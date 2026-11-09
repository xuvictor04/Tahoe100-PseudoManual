---
symbol: "GLA"
type: "gene"
col: 2245
ensembl_id: "ENSG00000102393"
name: "galactosidase alpha"
location: "Xq22.1"
module: 60
arm: "+"
pooled_cpm: 17.51
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# GLA

*galactosidase alpha* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (26 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 4.42× (z +17.6, q 0e+00, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.05 µM in 1 line (A-172 0.0880×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOD1]] (+0.64, fdr 7e-06), [[HSPA1B]] (+0.63, fdr 1e-05), [[HSPA1A]] (+0.62, fdr 1e-05); moves opposite to [[DET1]] (-0.53, fdr 3e-05), [[MRPS31P4]] (-0.53, fdr 3e-05), [[TAMM41]] (-0.52, fdr 6e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 26 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 26 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2245.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.42×** | +17.6 | 0e+00 | 44/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +16.7 | 0e+00 | 42/45 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **4.09×** | +15.8 | 0e+00 | 44/46 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.47×** | +14.7 | 0e+00 | 43/46 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.94×** | +13.9 | 6e-42 | 45/47 (PANC-1, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.88×** | +12.5 | 4e-34 | 43/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.09×** | +12.3 | 6e-33 | 34/45 (NCI-H460, J82, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.80×** | +12.2 | 2e-32 | 39/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.29×** | +9.0 | 1e-17 | 29/34 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.42×** | +9.0 | 2e-17 | 38/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **2.08×** | +8.6 | 3e-16 | 28/39 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.28×** | +8.3 | 3e-15 | 38/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **2.02×** | +8.3 | 4e-15 | 35/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.00×** | +7.9 | 2e-13 | 28/47 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.98×** | +7.8 | 3e-13 | 19/24 (A549, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.63×** | +7.4 | 4e-12 | 36/48 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +6.6 | 2e-09 | 29/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.4 | 4e-09 | 23/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.80×** | +3.6 | 0.005 | 13/45 (HT-29, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.020 | 17/47 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2245.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.05 µM in 1 line (A-172 0.0880×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.716× | -3.4 | 0.33 | 12/47 (A549, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.70 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.7 | 13 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +22.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.85× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 20.9 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.17× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 24.9 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 23.6 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.67× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 16.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 17.9 | 5 | 0 | [[Auranofin (drug)]] 5 µM 6.61× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 16.1 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 10.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.85× (z +12.0) | — |
| [[KATO III (line)]] | alt | 21.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +11.6) | — |
| [[LoVo (line)]] | wt | 8.47 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.28× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.62× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 22.7 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.14× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 8.36 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.92× (z +9.2) | — |
| [[J82 (line)]] | alt | 14.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +13.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.39× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 23.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.48× (z +9.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.75× (z +8.5) | — |
| [[A-172 (line)]] | wt | 4.82 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0880× (z -8.9) |
| [[A498 (line)]] | wt | 24.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 13.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.61× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOD1]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[HSPA1B]] | +0.63 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[HSPA1A]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[HSP90AA2P]] | +0.61 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[PSMB4]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SERPINH1]] | +0.58 | +0.39 / +0.63 | both halves | 6e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[HTATIP2]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DNAJA1]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[UBB]] | +0.57 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[SLC38A6]] | +0.57 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[SFXN5]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[MLLT11]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DET1]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[MRPS31P4]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[TAMM41]] | -0.52 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[MRPS31P5-1]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CEP63]] | -0.49 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[PKN1]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[RIOK1]] | -0.49 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[ZNF696]] | -0.48 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[ASB13]] | -0.48 | -0.46 / -0.38 | both halves | 6e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[TMEM216]] | -0.47 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[COG2]] | -0.47 | -0.37 / -0.37 | both halves | 8e-05 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[TRIM35]] | -0.47 | -0.51 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GLA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.2, -10.5); signed map (-24.7, -27.7). **Vector** length 83.8, 21.2% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial unfolded protein response (UPRmt)* (reactome, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.4 | +13.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.0 | +17.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.4 | +15.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +16.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.8 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +0.4 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.2 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | galactosidase alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,393,273-101,408,012 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GALA |
| Gene groups (HGNC) | Galactosidases alpha |
| Hallmark sets | PROTEIN_SECRETION, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, MTORC1_SIGNALING |
| Reactome | 6 pathways, smallest: Glycosphingolipid catabolism; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P06280](https://www.uniprot.org/uniprotkb/P06280) (Alpha-galactosidase A):

> Catalyzes the hydrolysis of glycosphingolipids and participates in their degradation in the lysosome.

**Summary**, from NCBI Gene [2717](https://www.ncbi.nlm.nih.gov/gene/2717):

> This gene encodes a homodimeric glycoprotein that hydrolyses the terminal alpha-galactosyl moieties from glycolipids and glycoproteins. This enzyme predominantly hydrolyzes ceramide trihexoside, and it can catalyze the hydrolysis of melibiose into galactose and glucose. A variety of mutations in this gene affect the synthesis, processing, and stability of this enzyme, which causes Fabry disease, a rare lysosomal storage disorder that results from a failure to catabolize alpha-D-galactosyl …

**Accessions** — [HGNC:4296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4296) · Entrez [2717](https://www.ncbi.nlm.nih.gov/gene/2717) · UniProt [P06280](https://www.uniprot.org/uniprotkb/P06280) · Ensembl [ENSG00000102393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102393)

## Data

Gene col 2245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2245); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2245]; `tensor/DDL_lfc|DDL_z.npy` [2245]; `embed/gene_vectors.npy` [2245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2245 or target_col == 2245). Every well: [[GLA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
