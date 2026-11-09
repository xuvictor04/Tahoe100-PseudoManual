---
symbol: "TTC38"
type: "gene"
col: 1107
ensembl_id: "ENSG00000075234"
name: "tetratricopeptide repeat domain 38"
location: "22q13.31"
module: 17
arm: "+"
pooled_cpm: 18.51
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TTC38

*tetratricopeptide repeat domain 38* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.82× (z +10.3, q 4e-22, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.437× (z -20.2, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL26]] (+0.75, fdr 7e-06), [[MIGA2]] (+0.68, fdr 3e-05), [[WRAP73]] (+0.65, fdr 3e-05); moves opposite to [[CRPPA]] (-0.68, fdr 3e-05), [[HCG17]] (-0.67, fdr 1e-05), [[CCDC90B-AS1]] (-0.64, fdr 5e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +10.3 | 4e-22 | 34/47 (SW480, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +9.2 | 7e-18 | 37/47 (Hs 766T, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +5.7 | 3e-06 | 23/47 (Hs 766T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 6e-04 | 17/44 (SHP-77, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1107.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.437×** | -20.2 | 0e+00 | 41/46 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.549×** | -10.0 | 7e-21 | 34/46 (SW480, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.677×** | -9.6 | 2e-19 | 31/48 (Hs 766T, hTERT-HPNE, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -7.4 | 2e-11 | 30/46 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.659×** | -6.7 | 3e-09 | 19/36 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -5.6 | 2e-06 | 19/31 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **0.756×** | -4.8 | 1e-04 | 19/39 (SW1417, SW480, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -4.6 | 4e-04 | 21/47 (C32, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.766×** | -4.4 | 6e-04 | 17/45 (J82, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.637×** | -4.1 | 0.003 | 17/47 (SNU-1, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.790×** | -3.9 | 0.004 | 17/47 (COLO 205, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.797×** | -3.9 | 0.004 | 12/47 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.5 | 0.022 | 12/48 (A549, A498, …) | top dose only | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.830×** | -3.2 | 0.051 | 12/47 (A498, AsPC-1, …) | two highest doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.840× | -3.0 | 0.097 | 7/48 (AsPC-1, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0622× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0742× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -9.5) |
| [[A549 (line)]] | wt | 16.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -13.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 24.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -14.8) |
| [[HS-578T (line)]] | alt | 19.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -11.1) |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -11.0) |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -10.0) |
| [[A498 (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.386× (z -8.6) ⚠ cell-cycle shift, explains ~1% of this change |
| [[AsPC-1 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[C-33 A (line)]] | alt | 26.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -11.0) |
| [[C32 (line)]] | wt | 28.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -17.5) |
| [[HCT15 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -9.7) |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.364× (z -8.9) |
| [[J82 (line)]] | alt | 9.87 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0831× (z -13.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 17.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -16.3) |
| [[LoVo (line)]] | wt | 21.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -10.2) |
| [[LS 180 (line)]] | wt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.382× (z -9.4) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 16.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -8.8) |
| [[SW 900 (line)]] | alt | 24.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -14.4) |
| [[SW48 (line)]] | wt | 32.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -8.5) |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL26]] | +0.75 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MIGA2]] | +0.68 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[WRAP73]] | +0.65 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[RNF41]] | +0.64 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[MRPS31P4]] | +0.64 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[MAST3]] | +0.63 | +0.43 / +0.47 | both halves | 4e-05 |  |
| [[COMMD2]] | +0.63 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[PIGH]] | +0.63 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[RSAD1]] | +0.63 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[DPY30]] | +0.62 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[POLM]] | +0.62 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[BRAT1]] | +0.62 | +0.40 / +0.54 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRPPA]] | -0.68 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[HCG17]] | -0.67 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | -0.64 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[LINC02955]] | -0.62 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[MMADHC-DT]] | -0.60 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[SIAH2-AS1]] | -0.60 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[CIBAR1-DT]] | -0.60 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[RNF217-AS1]] | -0.59 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[EIF4G2]] | -0.59 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[C2orf88]] | -0.59 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[BHLHE40-AS1]] | -0.58 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[MKLN1-AS]] | -0.58 | -0.42 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TTC38's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers TTC38's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (1.1, -2.8); signed map (-35.0, -0.2). **Vector** length 93.6, 19.0% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.2 | +10.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +9.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +4.6 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.3 | +2.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -20.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.8 | -9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -10.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.6 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -4.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -3.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:46,267,961-46,294,008 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20699 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q5R3I4](https://www.uniprot.org/uniprotkb/Q5R3I4) carries no function annotation.

**Summary**, from NCBI Gene [55020](https://www.ncbi.nlm.nih.gov/gene/55020):

> Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26082) · Entrez [55020](https://www.ncbi.nlm.nih.gov/gene/55020) · UniProt [Q5R3I4](https://www.uniprot.org/uniprotkb/Q5R3I4) · Ensembl [ENSG00000075234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075234)

## Data

Gene col 1107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1107); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1107]; `tensor/DDL_lfc|DDL_z.npy` [1107]; `embed/gene_vectors.npy` [1107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1107 or target_col == 1107). Every well: [[TTC38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
