---
symbol: "ECI2"
type: "gene"
col: 12653
ensembl_id: "ENSG00000198721"
name: "enoyl-CoA delta isomerase 2"
location: "6p25.2"
module: 30
arm: "+"
pooled_cpm: 33.93
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ECI2

*enoyl-CoA delta isomerase 2* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.41× (z +4.7, q 0.001, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.220× (z -29.1, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VDAC3]] (+0.76, fdr 7e-06), [[HACE1]] (+0.71, fdr 3e-05), [[HEBP1]] (+0.68, fdr 1e-05); moves opposite to [[ZC3H4]] (-0.72, fdr 7e-06), [[PCF11]] (-0.72, fdr 1e-05), [[LEKR1]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12653.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +4.7 | 0.001 | 23/46 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +4.5 | 0.002 | 23/47 (HS-578T, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.39×** | +4.5 | 0.002 | 24/43 (SHP-77, A498, …) | two highest doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.009 | 21/47 (PANC-1, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12653.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.220×** | -29.1 | 0e+00 | 44/47 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.323×** | -15.3 | 0e+00 | 42/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.320×** | -14.9 | 0e+00 | 41/47 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.365×** | -6.4 | 2e-08 | 35/47 (HOP62, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -6.4 | 2e-08 | 32/46 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -6.3 | 2e-08 | 38/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -6.3 | 3e-08 | 35/47 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.427×** | -5.4 | 5e-06 | 29/47 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.679×** | -5.2 | 1e-05 | 30/47 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.732×** | -4.2 | 0.001 | 27/46 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.739×** | -3.9 | 0.006 | 19/46 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.755×** | -3.8 | 0.007 | 24/47 (SNU-423, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.775×** | -3.3 | 0.040 | 20/47 (LoVo, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 79.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -26.7) |
| [[Panc 03.27 (line)]] | alt | 32.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -18.8) |
| [[SNU-423 (line)]] | alt | 80.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -31.9) |
| [[A549 (line)]] | wt | 34.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 27.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -19.7) |
| [[HCT15 (line)]] | alt | 46.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0592× (z -27.9) |
| [[HOP62 (line)]] | alt | 58.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0729× (z -38.6) |
| [[HS-578T (line)]] | alt | 37.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -18.3) |
| [[hTERT-HPNE (line)]] | wt | 38.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -18.0) |
| [[J82 (line)]] | alt | 65.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0721× (z -34.0) |
| [[NCI-H2030 (line)]] | alt | 44.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -25.5) |
| [[NCI-H2347 (line)]] | alt | 44.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -24.1) |
| [[NCI-H460 (line)]] | wt | 21.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -22.1) |
| [[PANC-1 (line)]] | alt | 26.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -21.1) |
| [[SK-MEL-2 (line)]] | alt | 35.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0881× (z -26.6) |
| [[A498 (line)]] | wt | 31.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -12.4) |
| [[AN3 CA (line)]] | alt | 66.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -12.6) |
| [[C32 (line)]] | wt | 34.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -20.7) |
| [[H4 (line)]] | wt | 25.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0608× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -17.5) |
| [[KATO III (line)]] | alt | 10.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.259× (z -8.6) |
| [[LoVo (line)]] | wt | 11.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 41.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -21.7) |
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -20.8) |
| [[NCI-H1792 (line)]] | alt | 27.0 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 37.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -20.6) |
| [[RPMI-7951 (line)]] | alt | 29.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -17.9) |
| [[SNU-1 (line)]] | wt | 46.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -8.9) |
| [[SW 1271 (line)]] | alt | 42.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0788× (z -8.9) |
| [[SW 900 (line)]] | alt | 36.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 27.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.3) |
| [[COLO 205 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -8.6) |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.7) |
| [[LS 180 (line)]] | wt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.3) |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0883× (z -9.1) |
| [[SW48 (line)]] | wt | 38.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -11.2) |
| [[A-427 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VDAC3]] | +0.76 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[HACE1]] | +0.71 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[HEBP1]] | +0.68 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MMS19]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[NBPF3]] | +0.68 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[MGST3]] | +0.67 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.67 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.67 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.66 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[MACO1]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[RGS10]] | +0.66 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H4]] | -0.72 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[PCF11]] | -0.72 | -0.73 / -0.49 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.71 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[ST7L]] | -0.70 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.69 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | -0.69 | -0.70 / -0.45 | both halves | 3e-05 |  |
| [[EXOSC6]] | -0.68 | -0.71 / -0.48 | both halves | 2e-05 |  |
| [[PPP3CB-AS1]] | -0.68 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[SKIL]] | -0.67 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[CHTOP]] | -0.66 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[FKRP]] | -0.65 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[INO80D]] | -0.64 | -0.63 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises ECI2's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.49× lower at baseline in the lines without KATNAL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[SNTA1]] | B | SNTA1 activity raises ECI2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 2.69× lower at baseline in the lines without SNTA1 | 0.039 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (2.0, -9.9); signed map (-34.5, -5.6). **Vector** length 102, 25.2% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +0.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.9 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -29.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -14.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | enoyl-CoA delta isomerase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:4,115,693-4,135,597 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ACBD2, DRS1, HCA88; previously PECI |
| Hallmark sets | PEROXISOME, FATTY_ACID_METABOLISM |
| Reactome | 6 pathways, smallest: Beta-oxidation of very long chain fatty acids; Peroxisomal lipid metabolism; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [O75521](https://www.uniprot.org/uniprotkb/O75521) (Enoyl-CoA delta isomerase 2):

> Auxiliary enzyme in the beta-oxidation of mono- and polyunsaturated fatty acids. Together with the 2,4-dienoyl-CoA reductase (DECR) and the Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase (ECH), they allow the reentrance of the enoyl-CoA into the beta-oxidation cycle. Able to isomerize both 3-cis (3Z) and 3-trans (3E) double bonds into the 2-trans (2E) form in a range of fatty enoyl-CoA species, with a preference for (3E)-enoyl-CoAs over (3Z)-enoyl-CoAs. Based on its established catalytic …

**Summary**, from NCBI Gene [10455](https://www.ncbi.nlm.nih.gov/gene/10455):

> This gene encodes a member of the hydratase/isomerase superfamily. The protein encoded is a key mitochondrial enzyme involved in beta-oxidation of unsaturated fatty acids. It catalyzes the transformation of 3-cis and 3-trans-enoyl-CoA esters arising during the stepwise degradation of cis-, mono-, and polyunsaturated fatty acids to the 2-trans-enoyl-CoA intermediates. Alternatively spliced transcript variants have been described. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:14601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14601) · Entrez [10455](https://www.ncbi.nlm.nih.gov/gene/10455) · UniProt [O75521](https://www.uniprot.org/uniprotkb/O75521) · Ensembl [ENSG00000198721](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198721)

## Data

Gene col 12653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12653); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12653]; `tensor/DDL_lfc|DDL_z.npy` [12653]; `embed/gene_vectors.npy` [12653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12653 or target_col == 12653). Every well: [[ECI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
