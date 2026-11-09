---
symbol: "LHFPL3"
type: "gene"
col: 11913
ensembl_id: "ENSG00000187416"
name: "LHFPL tetraspan subfamily member 3"
location: "7q22.2-q22.3"
module: 26
arm: "+"
pooled_cpm: 8.31
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# LHFPL3

*LHFPL tetraspan subfamily member 3* — 7q22.2-q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.07× (z +25.6, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Quinestrol (drug)]] 5 µM: 0.809× (z -3.8, q 0.072, down in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.05 µM in 1 line (NCI-H23 0.0513×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (J82 0.0837×); [[Raltitrexed (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0795×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01090]] (+0.80, fdr 7e-06), [[INTS6-AS1]] (+0.75, fdr 1e-05), [[SYNM-AS1]] (+0.74, fdr 7e-06); moves opposite to [[WRAP73]] (-0.70, fdr 2e-05), [[SLC39A3]] (-0.70, fdr 3e-05), [[NAA40]] (-0.63, fdr 8e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11913.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.07×** | +25.6 | 0e+00 | 42/42 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.25×** | +14.8 | 0e+00 | 33/42 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.95×** | +13.9 | 6e-42 | 28/31 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +13.2 | 2e-37 | 11/15 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.25×** | +10.5 | 1e-23 | 36/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +10.3 | 8e-23 | 19/24 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.4 | 2e-11 | 27/43 (KATO III, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +6.4 | 8e-09 | 24/45 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +6.4 | 8e-09 | 22/41 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.5 | 2e-06 | 19/42 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +5.5 | 2e-06 | 14/39 (HS-578T, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.1 | 1e-05 | 16/48 (A-172, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.8 | 0.007 | 12/37 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.015 | 11/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.036 | 11/46 (A-427, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.059 | 5/46 (SW480, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11913.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.05 µM in 1 line (NCI-H23 0.0513×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (J82 0.0837×); [[Raltitrexed (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0795×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Quinestrol (drug)]] 5 µM |  | **0.809×** | -3.8 | 0.072 | 15/48 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.753×** | -3.6 | 0.074 | 15/47 (SK-MEL-2, C32, …) | two highest doses |  |
| [[OTS514 (drug)]] 5 µM |  | 0.618× | -3.2 | 0.17 | 8/32 (AsPC-1, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Quinestrol (drug)]] 0.5 µM |  | 0.777× | -3.2 | 0.17 | 7/47 (SHP-77, SW 900, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.06 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +11.7) | — |
| [[LoVo (line)]] | wt | 9.45 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +12.5) | — |
| [[A498 (line)]] | wt | 5.34 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.96× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 5.52 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +10.4) | [[Nimesulide (drug)]] 5 µM 0.0765× (z -9.6) ⚠ toxic; unreliable plate only |
| [[J82 (line)]] | alt | 5.45 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +8.8) | [[Monocrotaline (drug)]] 0.05 µM 0.0837× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 7.50 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 5.53 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +9.2) | [[Raltitrexed (drug)]] 0.5 µM 0.0795× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 6.36 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.48× (z +11.0) | — |
| [[RKO (line)]] | wt | 8.64 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.127× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.16× (z +9.2) | — |
| [[A549 (line)]] | wt | 5.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 6.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 5.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.52× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 8.01 | 0 | 1 | — | [[Meloxicam (drug)]] 0.5 µM 0.0620× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 6.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 6.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 9.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 7.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 6.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 7.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +10.3) | — |
| [[KATO III (line)]] | alt | 7.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 7.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.25 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0879× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 7.15 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0513× (z -11.9) |
| [[PANC-1 (line)]] | alt | 6.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +10.7) | — |
| [[SW480 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +11.1) | — |
| [[A-427 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01090]] | +0.80 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.75 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[SYNM-AS1]] | +0.74 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.73 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[TMEM202-AS1]] | +0.72 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[EYS]] | +0.72 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PSMD14-DT]] | +0.71 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[PSMD7-DT]] | +0.71 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[MALINC1]] | +0.71 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[CIBAR1-DT]] | +0.71 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[DPP6]] | +0.70 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CFAP418-AS1]] | +0.70 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.70 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SLC39A3]] | -0.70 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[NAA40]] | -0.63 | -0.52 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LHFPL3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.4, 18.9); signed map (28.2, -4.1). **Vector** length 69.2, 10.6% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.8 | +25.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | -0.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.1 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.3 |
|  | [[Quinestrol (drug)]] 5 µM |  | -0.8 | -3.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.8 | +0.3 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -0.8 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -0.7 |
|  | [[Rimonabant (drug)]] 5 µM |  | -0.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | LHFPL tetraspan subfamily member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.2-q22.3 — chr7:104,328,603-104,908,561 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LHFPL4 |
| Gene groups (HGNC) | LHFPL tetraspan proteins |
| Matched by | ensembl_id |

UniProt [Q86UP9](https://www.uniprot.org/uniprotkb/Q86UP9) carries no function annotation.

**Summary**, from NCBI Gene [375612](https://www.ncbi.nlm.nih.gov/gene/375612):

> This gene is a member of the lipoma HMGIC fusion partner (LHFP) gene family, which is a subset of the superfamily of tetraspan transmembrane protein encoding genes. Mutations in one LHFP-like gene result in deafness in humans and mice, and a second LHFP-like gene is fused to a high-mobility group gene in a translocation-associated lipoma. A partial gene fragment named LHFPL4 corresponds to a portion of the first exon of this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6589) · Entrez [375612](https://www.ncbi.nlm.nih.gov/gene/375612) · UniProt [Q86UP9](https://www.uniprot.org/uniprotkb/Q86UP9) · Ensembl [ENSG00000187416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187416)

## Data

Gene col 11913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11913); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11913]; `tensor/DDL_lfc|DDL_z.npy` [11913]; `embed/gene_vectors.npy` [11913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11913 or target_col == 11913). Every well: [[LHFPL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHFPL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
