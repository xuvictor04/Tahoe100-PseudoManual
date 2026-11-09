---
symbol: "LYRM1"
type: "gene"
col: 2285
ensembl_id: "ENSG00000102897"
name: "LYR motif containing 1"
location: "16p12.3"
module: 26
arm: "+"
pooled_cpm: 23.52
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# LYRM1

*LYR motif containing 1* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +18.6, q 0e+00, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.634× (z -9.8, q 5e-20, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5D2]] (+0.68, fdr 2e-05), [[CROCC]] (+0.63, fdr 1e-04), [[FBXL19-AS1]] (+0.61, fdr 1e-04); moves opposite to [[WRAP73]] (-0.66, fdr 4e-05), [[MRPS34]] (-0.63, fdr 1e-04), [[GPATCH11]] (-0.62, fdr 2e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +18.6 | 0e+00 | 38/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +16.4 | 0e+00 | 34/42 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +16.2 | 0e+00 | 27/33 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +14.3 | 4e-44 | 32/37 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +13.6 | 8e-40 | 29/47 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +10.8 | 3e-25 | 31/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +7.0 | 3e-10 | 25/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +6.9 | 5e-10 | 21/47 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.8 | 8e-10 | 19/46 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +6.3 | 1e-08 | 25/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +5.8 | 4e-07 | 19/47 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 5e-06 | 17/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +5.0 | 2e-05 | 15/47 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.8 | 5e-05 | 17/47 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.21×** | +4.1 | 0.002 | 11/47 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.005 | 17/47 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.013 | 7/48 (A498, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.013 | 2/47 (AsPC-1, SK-MEL-2) | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.026 | 6/46 (CFPAC-1, H4, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2285.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.634×** | -9.8 | 5e-20 | 34/48 (COLO 205, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.653×** | -9.2 | 1e-17 | 30/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.700×** | -7.7 | 3e-12 | 27/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.822×** | -4.2 | 0.003 | 13/48 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.754×** | -3.7 | 0.024 | 8/46 (CFPAC-1, SW 900, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.723×** | -3.7 | 0.024 | 10/45 (RPMI-7951, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.855× | -3.4 | 0.056 | 10/45 (RKO, SW1417, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.853× | -3.3 | 0.065 | 13/46 (CHP-212, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 19.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +13.6) | — |
| [[LoVo (line)]] | wt | 13.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.7× (z +19.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +13.3) | — |
| [[SW1417 (line)]] | alt | 70.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 20.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.30× (z +11.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 3 | — | [[Saquinavir (drug)]] 0.5 µM 0.103× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 19.1 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 13.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.8× (z +13.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 44.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 35.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.26× (z +13.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 22.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.81× (z +13.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 26.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 25.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 63.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -8.9) |
| [[A498 (line)]] | wt | 37.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.1× (z +8.8) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.05 µM 0.0573× (z -9.1) |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -11.9) |
| [[HOP62 (line)]] | alt | 8.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0608× (z -17.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5D2]] | +0.68 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[CROCC]] | +0.63 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[FBXL19-AS1]] | +0.61 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[CHMP3]] | +0.61 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[HIVEP2-DT]] | +0.60 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[CCDC200]] | +0.59 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[LHFPL3]] | +0.59 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[KMT2E-AS1]] | +0.58 | +0.42 / +0.29 | both halves | 2e-04 |  |
| [[PSMD6-AS1]] | +0.57 | +0.37 / +0.42 | both halves | 9e-05 |  |
| [[PHF8]] | +0.57 | +0.42 / +0.37 | both halves | 8e-05 |  |
| [[AKT1S1]] | +0.57 | +0.37 / +0.39 | both halves | 9e-05 |  |
| [[SUMO2P17]] | +0.57 | +0.43 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.66 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[MRPS34]] | -0.63 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[GPATCH11]] | -0.62 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[MRPL17]] | -0.62 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[POP7]] | -0.62 | -0.32 / -0.64 | both halves | 2e-04 |  |
| [[MTMR12]] | -0.62 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[MALSU1]] | -0.61 | -0.36 / -0.57 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.60 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[MRPL55]] | -0.58 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[MAP1S]] | -0.58 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[PET117]] | -0.58 | -0.22 / -0.58 | both halves | 6e-04 |  |
| [[C1orf35]] | -0.58 | -0.39 / -0.62 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises LYRM1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.524). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (7.4, 8.6); signed map (33.6, -19.5). **Vector** length 97.0, 20.6% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.0 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.7 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.1 | +16.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +18.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.2 | +0.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.5 | -7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -9.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | -9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.0 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | LYR motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:20,899,868-20,925,006 (+) |
| Ensembl biotype | protein_coding |
| Also known as | A211C6.1 |
| Gene groups (HGNC) | LYR motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43325](https://www.uniprot.org/uniprotkb/O43325) (LYR motif-containing protein 1):

> May promote cell proliferation and inhibition of apoptosis of preadipocytes.

**Summary**, from NCBI Gene [57149](https://www.ncbi.nlm.nih.gov/gene/57149):

> The protein encoded by this gene belongs to the mitochondrial leucine/tyrosine/arginine motif family of proteins. Proteins of this family are short polypeptides that contain a leucine/tyrosine/arginine motif near the N-terminus. This gene is widely expressed with high levels in omental adipose tissue of obese individuals. In adipose tissue, the protein is localized to the nucleus where it promotes preadipocyte proliferation and lowers the rate of apoptosis to regulate adipose tissue …

**Accessions** — [HGNC:25074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25074) · Entrez [57149](https://www.ncbi.nlm.nih.gov/gene/57149) · UniProt [O43325](https://www.uniprot.org/uniprotkb/O43325) · Ensembl [ENSG00000102897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102897)

## Data

Gene col 2285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2285); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2285]; `tensor/DDL_lfc|DDL_z.npy` [2285]; `embed/gene_vectors.npy` [2285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2285 or target_col == 2285). Every well: [[LYRM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYRM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
