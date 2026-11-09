---
symbol: "SNHG1"
type: "gene"
col: 14955
ensembl_id: "ENSG00000255717"
name: "small nucleolar RNA host gene 1"
location: "11q12.3"
module: 20
arm: "-"
pooled_cpm: 34.5
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 2
n_dd_up_clean: 27
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SNHG1

*small nucleolar RNA host gene 1* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.50× (z +17.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.615× (z -4.7, q 0.001, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFAS1]] (+0.67, fdr 7e-06), [[SNHG12]] (+0.66, fdr 7e-06), [[TAF1D]] (+0.61, fdr 7e-06); moves opposite to [[ERGIC2]] (-0.63, fdr 1e-05), [[YWHAB]] (-0.55, fdr 3e-05), [[ACTR2]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.50×** | +17.1 | 0e+00 | 47/48 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.48×** | +14.5 | 3e-45 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.37×** | +11.8 | 7e-30 | 38/47 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.78×** | +9.9 | 6e-21 | 45/47 (SW480, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.76×** | +9.8 | 1e-20 | 47/48 (SW480, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.71×** | +9.3 | 2e-18 | 41/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.61×** | +9.3 | 2e-18 | 41/47 (HT-29, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +9.1 | 8e-18 | 44/48 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.41×** | +8.5 | 1e-15 | 44/47 (SW480, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +8.2 | 1e-14 | 41/46 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.40×** | +8.1 | 2e-14 | 41/47 (A-427, HEC-1-A, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.98×** | +6.6 | 2e-09 | 40/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.1 | 5e-08 | 33/48 (HOP62, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +5.7 | 4e-07 | 34/48 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +5.5 | 1e-06 | 30/48 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **2.89×** | +5.4 | 3e-06 | 40/48 (Panc 03.27, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +5.2 | 7e-06 | 34/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +4.6 | 1e-04 | 32/47 (SW480, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.40×** | +4.4 | 3e-04 | 33/47 (SW480, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.37×** | +4.4 | 3e-04 | 32/46 (AsPC-1, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 4e-04 | 30/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14955.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.615×** | -4.7 | 0.001 | 35/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | **0.754×** | -3.9 | 0.033 | 29/48 (SW480, LS 180, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 20.7 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +13.7) | — |
| [[SW480 (line)]] | alt | 51.1 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.38× (z +17.8) | — |
| [[LoVo (line)]] | wt | 50.3 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 27.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.73× (z +17.9) | — |
| [[C32 (line)]] | wt | 19.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.77× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 24.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.50× (z +13.7) | — |
| [[HT-29 (line)]] | alt | 37.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +13.5) | — |
| [[LOX-IMVI (line)]] | wt | 41.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 53.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +13.0) | — |
| [[A-172 (line)]] | wt | 11.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.38× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 44.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 19.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.58× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 28.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.0) | — |
| [[KATO III (line)]] | alt | 32.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 17.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.01× (z +9.5) | — |
| [[RKO (line)]] | wt | 41.1 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.06× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 32.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.43× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 64.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +12.0) | — |
| [[A-427 (line)]] | wt | 56.1 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +9.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.06× (z +9.0) | — |
| [[A498 (line)]] | wt | 25.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +10.3) | — |
| [[A549 (line)]] | wt | 26.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +12.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.7 | 2 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 7.47× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 40.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.26× (z +16.5) | — |
| [[SW 900 (line)]] | alt | 26.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.08× (z +12.8) | — |
| [[BT-474 (line)]] | alt | 24.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 39.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 23.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.46× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +10.7) | — |
| [[J82 (line)]] | alt | 34.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.86× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 19.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.11× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 29.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 41.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +13.3) | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFAS1]] | +0.67 | +0.71 / +0.66 | both halves | 7e-06 | same gene group |
| [[SNHG12]] | +0.66 | +0.68 / +0.69 | both halves | 7e-06 | same gene group |
| [[TAF1D]] | +0.61 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[GAS5]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 | same gene group |
| [[FAM219B]] | +0.59 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SNHG7]] | +0.58 | +0.68 / +0.60 | both halves | 7e-06 | same gene group |
| [[NXF1]] | +0.58 | +0.67 / +0.44 | both halves | 3e-05 | ⚠ same locus (45.7 kb, same strand: neighbours can correlate without regulation) |
| [[RCC1]] | +0.57 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TUBE1]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RBCK1]] | +0.56 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[EPB41L4A-AS1]] | +0.56 | +0.61 / +0.56 | both halves | 1e-05 | same gene group |
| [[ZFPL1]] | +0.55 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[TIAL1]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERGIC2]] | -0.63 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[YWHAB]] | -0.55 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[ACTR2]] | -0.55 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[RANBP6]] | -0.54 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[PURB]] | -0.49 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[AP1B1]] | -0.48 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[AKIRIN1]] | -0.48 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[FBXO36]] | -0.48 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[NF2]] | -0.47 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[MAP3K14]] | -0.47 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[ROCK2]] | -0.46 | -0.29 / -0.46 | both halves | 3e-04 |  |
| [[VCL]] | -0.46 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SNHG1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.0158). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.2, -29.1); signed map (-15.2, -2.1). **Vector** length 87.6, 27.6% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.4 | +8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +9.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +5.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | +0.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +1.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -4.0 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | +1.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.5 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | +1.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q12.3 — chr11:62,851,978-62,855,953 (-) |
| Ensembl biotype | lncRNA |
| Also known as | UHG, NCRNA00057, LINC00057, lncRNA16 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [23642](https://www.ncbi.nlm.nih.gov/gene/23642):

> This locus represents a small nucleolar RNA host gene that produces multiple alternatively spliced long non-coding RNAs. This gene is upregulated in cancers and is thought to act as promoter of cell proliferation. This transcript negatively regulates tumor suppressor genes such as tumor protein p53. Expression of this locus may be a marker of tumor progression. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:32688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32688) · Entrez [23642](https://www.ncbi.nlm.nih.gov/gene/23642) · Ensembl [ENSG00000255717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255717)

## Data

Gene col 14955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14955); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14955]; `tensor/DDL_lfc|DDL_z.npy` [14955]; `embed/gene_vectors.npy` [14955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14955 or target_col == 14955). Every well: [[SNHG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
