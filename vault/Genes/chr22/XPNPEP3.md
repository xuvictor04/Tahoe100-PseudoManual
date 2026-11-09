---
symbol: "XPNPEP3"
type: "gene"
col: 12163
ensembl_id: "ENSG00000196236"
name: "X-prolyl aminopeptidase 3"
location: "22q13.2"
module: 52
arm: "+"
pooled_cpm: 51.67
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# XPNPEP3

*X-prolyl aminopeptidase 3* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.78× (z +12.5, q 8e-33, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.673× (z -8.3, q 7e-14, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.810× (z -6.5, q 1e-08, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC30A6]] (+0.71, fdr 7e-06), [[APTX]] (+0.68, fdr 7e-06), [[VPS53]] (+0.67, fdr 7e-06); moves opposite to [[PTGER4]] (-0.53, fdr 3e-05), [[TBL1XR1]] (-0.53, fdr 1e-05), [[CTNNB1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12163.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +12.5 | 8e-33 | 42/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +7.1 | 3e-10 | 30/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +6.7 | 4e-09 | 30/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +6.4 | 2e-08 | 30/48 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.26×** | +4.7 | 2e-04 | 26/48 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.003 | 19/48 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.037 | 13/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.066 | 12/48 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.12 | 14/47 (HS-578T, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trimetrexate (drug)]] 5 µM |  | 1.10× | +3.0 | 0.14 | 3/48 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.673×** | -8.3 | 7e-14 | 33/48 (AN3 CA, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.805×** | -6.7 | 5e-09 | 23/48 (A498, A549, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.737×** | -6.7 | 5e-09 | 26/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -6.5 | 1e-08 | 31/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.756×** | -6.1 | 1e-07 | 24/48 (SW480, H4, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.788×** | -5.0 | 5e-05 | 25/47 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.795×** | -5.0 | 5e-05 | 25/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.793×** | -4.7 | 2e-04 | 20/44 (A-427, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.821×** | -4.3 | 0.001 | 22/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.2 | 0.002 | 0/49 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.830×** | -4.1 | 0.002 | 21/48 (H4, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.740×** | -3.4 | 0.028 | 16/49 (SK-MEL-2, AsPC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | 0.858× | -3.2 | 0.059 | 17/43 (NCI-H1573, NCI-H23, …) | inconsistent across doses | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.763×** | -3.1 | 0.083 | 14/48 (LoVo, SNU-423, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 94.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -17.9) ⚠ cell-cycle shift, explains ~97% of this change |
| [[SK-MEL-2 (line)]] | alt | 171 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 38.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.36× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 50.8 | 0 | 2 (1 ⚠) | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.109× (z -11.3) |
| [[HOP62 (line)]] | alt | 43.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.15× (z +12.6) | [[Digitoxin (drug)]] 5 µM 0.381× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HS-578T (line)]] | alt | 82.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -10.3) ⚠ cell-cycle shift, explains ~97% of this change |
| [[hTERT-HPNE (line)]] | wt | 55.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.339× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H23 (line)]] | alt | 60.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.33× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[NCI-H460 (line)]] | wt | 46.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.365× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -10.3) ⚠ cell-cycle shift, explains ~97% of this change |
| [[HCT15 (line)]] | alt | 76.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 53.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.29× (z +10.0) | — |
| [[J82 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.5) ⚠ cell-cycle shift, explains ~97% of this change |
| [[KATO III (line)]] | alt | 72.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[NCI-H2030 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[PANC-1 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.465× (z -8.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SNU-423 (line)]] | alt | 33.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.89× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 48.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.92× (z +9.6) | — |
| [[SW480 (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.513× (z -9.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 74.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A6]] | +0.71 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[APTX]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[VPS53]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[NUP214]] | +0.64 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[STX16-NPEPL1]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[EARS2]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[SLC30A5]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[GNAS-AS1]] | +0.61 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[COG3]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[GOSR2]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[GON4L]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[DCAF10]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGER4]] | -0.53 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[TBL1XR1]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[CTNNB1]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[KSR1]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[TCF7L2]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ELAVL2]] | -0.51 | -0.38 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers XPNPEP3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DAB2IP]] | C | DAB2IP activity lowers XPNPEP3's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 1.10× higher at baseline in the lines without DAB2IP | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-11.6, 20.4); signed map (-47.1, 2.8). **Vector** length 102, 24.6% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.4 | +12.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.0 | +4.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.7 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.0 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.1 | -8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -4.3 | -6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.9 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Cyclosporin A (drug)]] 0.5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | X-prolyl aminopeptidase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:40,857,077-40,932,815 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APP3, NPHPL1, ICP55 |
| Gene groups (HGNC) | Aminopeptidases; M24 metallopeptidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQH7](https://www.uniprot.org/uniprotkb/Q9NQH7) (Xaa-Pro aminopeptidase 3):

> Catalyzes the removal of a penultimate prolyl residue from the N-termini of peptides, such as Leu-Pro-Ala. Also shows low activity towards peptides with Ala or Ser at the P1 position.; [Isoform 1]: Promotes TNFRSF1B-mediated phosphorylation of MAPK8/JNK1 and MAPK9/JNK2, suggesting a function as an adapter protein for TNFRSF1B; the effect is independent of XPNPEP3 peptidase activity. May inhibit apoptotic cell death induced via TNF-TNFRSF1B signaling.

**Summary**, from NCBI Gene [63929](https://www.ncbi.nlm.nih.gov/gene/63929):

> The protein encoded by this gene belongs to the family of X-pro-aminopeptidases that utilize a metal cofactor, and remove the N-terminal amino acid from peptides with a proline residue in the penultimate position. This protein has been shown to localize to the mitochondria of renal cells, and have a role in ciliary function. Mutations in this gene are associated with nephronophthisis-like nephropathy-1. Alternatively spliced transcript variants encoding different isoforms have been noted for …

**Accessions** — [HGNC:28052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28052) · Entrez [63929](https://www.ncbi.nlm.nih.gov/gene/63929) · UniProt [Q9NQH7](https://www.uniprot.org/uniprotkb/Q9NQH7) · Ensembl [ENSG00000196236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196236)

## Data

Gene col 12163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12163); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12163]; `tensor/DDL_lfc|DDL_z.npy` [12163]; `embed/gene_vectors.npy` [12163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12163 or target_col == 12163). Every well: [[XPNPEP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XPNPEP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
