---
symbol: "SCRN2"
type: "gene"
col: 6500
ensembl_id: "ENSG00000141295"
name: "secernin 2"
location: "17q21.32"
module: 58
arm: "+"
pooled_cpm: 5.28
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# SCRN2

*secernin 2* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.35× (z +7.1, q 9e-10, up in 5 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.45× (z +4.5, q 8e-04, up in 16 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.321× (z -9.8, q 6e-20, down in 33 of 37 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THYN1]] (+0.76, fdr 7e-06), [[TMEM141]] (+0.71, fdr 1e-05), [[MRPL43]] (+0.68, fdr 5e-05); moves opposite to [[PSMD6-AS1]] (-0.65, fdr 2e-05), [[SPON1-AS1]] (-0.64, fdr 1e-05), [[AVEN]] (-0.59, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PGM5P2-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +7.1 | 9e-10 | 5/10 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +5.1 | 1e-04 | 12/22 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +4.8 | 2e-04 | 14/28 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +4.5 | 8e-04 | 16/46 (KATO III, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +3.9 | 0.009 | 10/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6500.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.321×** | -9.8 | 6e-20 | 33/37 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.451×** | -9.7 | 8e-20 | 32/38 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.332×** | -9.5 | 4e-19 | 40/46 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.484×** | -8.8 | 1e-16 | 28/36 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.379×** | -8.4 | 7e-15 | 39/44 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.435×** | -7.2 | 7e-11 | 27/45 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.493×** | -5.8 | 7e-07 | 25/44 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.557×** | -5.1 | 3e-05 | 22/44 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.558×** | -4.8 | 8e-05 | 22/43 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -4.8 | 9e-05 | 23/38 (A-427, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.361×** | -3.8 | 0.008 | 13/42 (SW1417, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.370×** | -3.7 | 0.010 | 14/37 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -3.6 | 0.013 | 18/34 (SW 900, Hs 766T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.686×** | -3.3 | 0.045 | 13/45 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.684×** | -3.0 | 0.092 | 7/44 (HepG2/C3A, RPMI-7951, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.707×** | -3.0 | 0.097 | 16/43 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.55 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 8.38 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -10.1) |
| [[PANC-1 (line)]] | alt | 5.31 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0822× (z -17.6) |
| [[A-427 (line)]] | wt | 4.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0697× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 4.52 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0683× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 11.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -10.9) |
| [[LoVo (line)]] | wt | 2.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -9.7) |
| [[LS 180 (line)]] | wt | 6.27 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 2.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0561× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 7.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -8.8) |
| [[SHP-77 (line)]] | alt | 4.18 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.0379× (z -9.4) |
| [[SNU-423 (line)]] | alt | 5.62 | 0 | 1 | — | [[Clofarabine (drug)]] 0.5 µM 0.0662× (z -8.7) |
| [[A-172 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THYN1]] | +0.76 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TMEM141]] | +0.71 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MRPL43]] | +0.68 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[NDUFA12]] | +0.68 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[NME3]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[DNAJC19]] | +0.66 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ANTKMT]] | +0.66 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ACBD4]] | +0.65 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PAFAH1B3]] | +0.64 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[CDK5]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[TMEM256]] | +0.64 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ROGDI]] | +0.63 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6-AS1]] | -0.65 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SPON1-AS1]] | -0.64 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[AVEN]] | -0.59 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[GLIPR1-AS1]] | -0.58 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[PDK1-AS1]] | -0.57 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[PCNT]] | -0.57 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[PSMD6-AS2]] | -0.56 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[MSANTD2]] | -0.56 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[ELK4]] | -0.54 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[LINC01829]] | -0.54 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[ANXA2R-OT1]] | -0.54 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[MMADHC-DT]] | -0.54 | -0.40 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[PAK2]] | -0.54 | -0.37 / -0.47 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGM5P2-1]] | B | PGM5P2-1 activity raises SCRN2's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 1.18× lower at baseline in the lines without PGM5P2-1 | 0.099 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[GSTM4]] | C | GSTM4 activity raises SCRN2's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without GSTM4 | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-26.3, -4.6); signed map (-22.3, -4.9). **Vector** length 53.6, 8.02% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.1 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -0.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.1 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -8.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | secernin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,837,692-47,841,289 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Secernin family |
| Matched by | ensembl_id |

UniProt [Q96FV2](https://www.uniprot.org/uniprotkb/Q96FV2) carries no function annotation.

**Summary**, from NCBI Gene [90507](https://www.ncbi.nlm.nih.gov/gene/90507):

> Predicted to enable cysteine-type exopeptidase activity and dipeptidase activity. Predicted to be involved in proteolysis. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30381) · Entrez [90507](https://www.ncbi.nlm.nih.gov/gene/90507) · UniProt [Q96FV2](https://www.uniprot.org/uniprotkb/Q96FV2) · Ensembl [ENSG00000141295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141295)

## Data

Gene col 6500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6500); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6500]; `tensor/DDL_lfc|DDL_z.npy` [6500]; `embed/gene_vectors.npy` [6500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6500 or target_col == 6500). Every well: [[SCRN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCRN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
