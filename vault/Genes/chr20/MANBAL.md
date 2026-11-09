---
symbol: "MANBAL"
type: "gene"
col: 2125
ensembl_id: "ENSG00000101363"
name: "mannosidase beta like"
location: "20q11.23"
module: 16
arm: "+"
pooled_cpm: 21.55
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MANBAL

*mannosidase beta like* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.41× (z +7.3, q 1e-10, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.648× (z -13.6, q 2e-39, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRRD]] (+0.68, fdr 7e-06), [[ZBTB39]] (+0.65, fdr 7e-06), [[PIGO]] (+0.65, fdr 1e-05); moves opposite to [[TBC1D12]] (-0.59, fdr 1e-05), [[DNAJC1]] (-0.58, fdr 1e-05), [[NDUFA2]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +7.3 | 1e-10 | 24/47 (NCI-H1792, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.3 | 1e-10 | 14/30 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +6.7 | 5e-09 | 24/45 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +6.1 | 1e-07 | 21/42 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +5.7 | 2e-06 | 18/48 (A-172, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +5.5 | 5e-06 | 16/48 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 7e-06 | 16/48 (A498, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 9e-06 | 16/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +5.1 | 2e-05 | 0/48 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.17× | +4.9 | 5e-05 | 16/48 (SK-MEL-2, HS-578T, …) | top dose only | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.9 | 5e-05 | 15/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.8 | 7e-05 | 14/47 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.22×** | +4.3 | 8e-04 | 14/44 (KATO III, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.21×** | +3.8 | 0.006 | 13/36 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +3.7 | 0.007 | 11/47 (RKO, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.013 | 10/46 (A549, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Erlotinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.013 | 7/47 (hTERT-HPNE, SW 900, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.054 | 2/48 (Panc 03.27, CFPAC-1) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.054 | 7/47 (HS-578T, SNU-423, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2125.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -13.6 | 2e-39 | 35/47 (LS 180, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -7.9 | 9e-13 | 31/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -7.0 | 4e-10 | 25/48 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.749×** | -6.4 | 2e-08 | 23/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.766×** | -5.9 | 4e-07 | 18/48 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.802×** | -4.9 | 9e-05 | 18/48 (SW1417, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -4.9 | 9e-05 | 18/48 (SNU-423, CHP-212, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.8 | 0.012 | 11/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.852× | -3.6 | 0.024 | 17/47 (AN3 CA, CHP-212, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.804×** | -3.4 | 0.032 | 9/45 (hTERT-HPNE, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.902× | -3.2 | 0.060 | 4/48 (H4, NCI-H23, …) | top dose only |  |
| [[Silodosin (drug)]] 5 µM |  | 0.868× | -3.0 | 0.11 | 14/47 (C-33 A, C32, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | 0.771× | -3.0 | 0.11 | 5/48 (RPMI-7951, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 28.7 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -11.0) |
| [[A498 (line)]] | wt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.0) |
| [[KATO III (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -9.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.170× (z -11.1) |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 25.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -8.7) |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.108× (z -10.3) |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRRD]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[ZBTB39]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[PIGO]] | +0.65 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[VPS72]] | +0.64 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[TOP3B]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[USP19]] | +0.64 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[HUS1]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ZSCAN20]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[DRG2]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.63 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[DNAJC14]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[OCRL]] | +0.62 | +0.50 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D12]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[DNAJC1]] | -0.58 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.53 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[RPS6KA5]] | -0.53 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[FBXO11]] | -0.53 | -0.52 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MANBAL's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises MANBAL's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.9, -1.7); signed map (-1.4, -34.1). **Vector** length 71.6, 11.6% of its response variance represented; |z| ≥ 3 in 808 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | +4.2 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +7.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.3 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -13.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -7.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -2.6 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -4.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase beta like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:37,289,649-37,317,260 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1141E15.2 |
| Gene groups (HGNC) | Mannosidases type beta |
| Matched by | ensembl_id |

UniProt [Q9NQG1](https://www.uniprot.org/uniprotkb/Q9NQG1) carries no function annotation.

**Summary**, from NCBI Gene [63905](https://www.ncbi.nlm.nih.gov/gene/63905):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15799) · Entrez [63905](https://www.ncbi.nlm.nih.gov/gene/63905) · UniProt [Q9NQG1](https://www.uniprot.org/uniprotkb/Q9NQG1) · Ensembl [ENSG00000101363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101363)

## Data

Gene col 2125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2125); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2125]; `tensor/DDL_lfc|DDL_z.npy` [2125]; `embed/gene_vectors.npy` [2125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2125 or target_col == 2125). Every well: [[MANBAL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MANBAL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
