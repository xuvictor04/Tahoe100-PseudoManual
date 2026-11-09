---
symbol: "ATL2"
type: "gene"
col: 4121
ensembl_id: "ENSG00000119787"
name: "atlastin GTPase 2"
location: "2p22.2-p22.1"
module: 67
arm: "+"
pooled_cpm: 121.39
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# ATL2

*atlastin GTPase 2* — 2p22.2-p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.78× (z +9.6, q 5e-19, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.640× (z -7.2, q 3e-10, down in 33 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.705× (z -5.9, q 9e-07, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.287×, A498 0.330×, C-33 A 0.292×, AN3 CA 0.185×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 4 lines (SW48 0.280×, SW480 0.452×, Panc 03.27 0.400×, C32 0.332×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.261×, HCT15 0.361×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP43]] (+0.64, fdr 7e-06), [[C4orf46]] (+0.63, fdr 1e-05), [[NDC1]] (+0.63, fdr 7e-06); moves opposite to [[BCL10]] (-0.62, fdr 1e-05), [[CD163L1]] (-0.56, fdr 3e-05), [[ADRM1]] (-0.54, fdr 2e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDCA7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +9.6 | 5e-19 | 45/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +8.0 | 5e-13 | 44/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +7.6 | 7e-12 | 41/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +7.3 | 6e-11 | 42/47 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.3 | 4e-08 | 35/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.42×** | +5.9 | 4e-07 | 31/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +4.9 | 6e-05 | 29/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.5 | 5e-04 | 0/50 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.002 | 22/49 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.003 | 25/48 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.4 | 0.039 | 20/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.040 | 22/49 (BT-474, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4121.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.287×, A498 0.330×, C-33 A 0.292×, AN3 CA 0.185×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 4 lines (SW48 0.280×, SW480 0.452×, Panc 03.27 0.400×, C32 0.332×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.261×, HCT15 0.361×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.640×** | -7.2 | 3e-10 | 33/44 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.663×** | -6.9 | 2e-09 | 37/49 (A498, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -5.9 | 9e-07 | 41/48 (SW48, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.699×** | -5.3 | 2e-05 | 24/45 (A498, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | 0.834× | -3.1 | 0.25 | 20/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 174 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 103 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +12.4) | — |
| [[LoVo (line)]] | wt | 117 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +12.7) | — |
| [[SW48 (line)]] | wt | 352 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -16.9) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.280× (z -10.7) |
| [[A498 (line)]] | wt | 200 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -15.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 99.7 | 2 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.68× (z +10.9) ⚠ cell-cycle shift, explains ~9% of this change | [[Auranofin (drug)]] 5 µM 0.332× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 179 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.400× (z -9.6) |
| [[SW480 (line)]] | alt | 156 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.452× (z -10.3) |
| [[A549 (line)]] | wt | 138 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.0) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[AN3 CA (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -11.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 89.2 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.36× (z +8.7) ⚠ toxic | — |
| [[HCT15 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 79.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 98.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.0) | — |
| [[KATO III (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 94.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 124 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.494× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 99.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 128 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 300 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP43]] | +0.64 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[C4orf46]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[NDC1]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[CDCA3]] | +0.62 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SPAG5]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CKS1B]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[LMNB1]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[MAD2L1]] | +0.60 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[KIF22]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ECT2]] | +0.59 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TMPO]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[KIF20A]] | +0.59 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL10]] | -0.62 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[CD163L1]] | -0.56 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[ADRM1]] | -0.54 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[TUT7]] | -0.53 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[TBRG1]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[IER5]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[STK17A]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[MSANTD3]] | -0.51 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[ALOXE3]] | -0.51 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[GADD45A]] | -0.50 | -0.57 / -0.42 | both halves | 4e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[ZNF426]] | -0.50 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[ZNF611]] | -0.49 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7]] | B | CDCA7 activity raises ATL2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without CDCA7 | 0.013 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.9, -55.6); signed map (-47.9, -39.6). **Vector** length 103, 31.1% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.50 to 12); *G2/M checkpoint* (hallmark, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.1 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +3.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.4 | -1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +0.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.0 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.3 | +2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | atlastin GTPase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2-p22.1 — chr2:38,293,954-38,377,285 (-) |
| Ensembl biotype | protein_coding |
| Also known as | atlastin2; previously ARL6IP2 |
| Gene groups (HGNC) | Atlastins |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 3 pathways, smallest: Dengue Virus Genome Translation and Replication; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHH9](https://www.uniprot.org/uniprotkb/Q8NHH9) (Atlastin-2):

> Atlastin-2 (ATL2) is a membrane-anchored GTPase that mediates the GTP-dependent fusion of endoplasmic reticulum (ER) membranes, maintaining the continuous ER network. It facilitates the formation of three-way junctions where ER tubules intersect. Two atlastin-2 on neighboring ER tubules bind GTP and form loose homodimers through the GB1/RHD3-type G domains and 3HB regions. Upon GTP hydrolysis, the 3HB regions tighten, pulling the membranes together to drive their fusion. After fusion, the …

**Summary**, from NCBI Gene [64225](https://www.ncbi.nlm.nih.gov/gene/64225):

> Enables GTPase-dependent fusogenic activity. Involved in endoplasmic reticulum membrane fusion and endoplasmic reticulum tubular network membrane organization. Located in endoplasmic reticulum membrane. Is active in endoplasmic reticulum tubular network membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24047](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24047) · Entrez [64225](https://www.ncbi.nlm.nih.gov/gene/64225) · UniProt [Q8NHH9](https://www.uniprot.org/uniprotkb/Q8NHH9) · Ensembl [ENSG00000119787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119787)

## Data

Gene col 4121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4121); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4121]; `tensor/DDL_lfc|DDL_z.npy` [4121]; `embed/gene_vectors.npy` [4121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4121 or target_col == 4121). Every well: [[ATL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
