---
symbol: "TATDN2"
type: "gene"
col: 8035
ensembl_id: "ENSG00000157014"
name: "TatD DNase domain containing 2"
location: "3p25.3"
module: 50
arm: "+"
pooled_cpm: 25.07
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# TATDN2

*TatD DNase domain containing 2* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.83× (z +10.0, q 9e-21, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.675× (z -7.0, q 2e-09, down in 28 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 0.306×, NCI-H2347 0.523×, NCI-H1573 0.373×; ⚠ cell-cycle shift, explains ~60% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.168×; ⚠ cell-cycle shift, explains ~26% of this change); [[Allantoin (drug)]] 0.5 µM in 1 line (HCT15 0.161×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (COLO 205 0.102×); [[Tofacitinib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0635×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COLGALT1]] (+0.69, fdr 7e-06), [[RNF4]] (+0.66, fdr 7e-06), [[WDR5]] (+0.66, fdr 9e-06); moves opposite to [[BAZ2B]] (-0.61, fdr 3e-05), [[AKAP9]] (-0.61, fdr 9e-06), [[RSF1]] (-0.60, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[VASH1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8035.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +10.0 | 9e-21 | 39/48 (PANC-1, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +7.9 | 6e-13 | 31/47 (A-427, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.6 | 3e-06 | 22/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +4.5 | 0.001 | 20/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.27×** | +4.3 | 0.002 | 17/48 (A-427, Hs 766T, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +4.2 | 0.002 | 15/47 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.22×** | +3.6 | 0.022 | 14/48 (HT-29, SNU-423, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.21×** | +3.5 | 0.028 | 13/48 (LS 180, SW1417, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8035.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 0.306×, NCI-H2347 0.523×, NCI-H1573 0.373×; ⚠ cell-cycle shift, explains ~60% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.168×; ⚠ cell-cycle shift, explains ~26% of this change); [[Allantoin (drug)]] 0.5 µM in 1 line (HCT15 0.161×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (COLO 205 0.102×); [[Tofacitinib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0635×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.675×** | -7.0 | 2e-09 | 28/47 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.790×** | -6.2 | 2e-07 | 28/47 (C32, NCI-H2347, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.731×** | -5.8 | 1e-06 | 23/47 (NCI-H2347, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.813×** | -3.8 | 0.016 | 19/48 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.674×** | -3.8 | 0.016 | 14/46 (hTERT-HPNE, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.850× | -3.4 | 0.066 | 10/48 (Hs 766T, SW 1088, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.867× | -3.1 | 0.13 | 10/48 (NCI-H1573, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.845× | -3.1 | 0.13 | 11/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | 0.728× | -3.1 | 0.14 | 11/42 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 21.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0791× (z -11.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 30.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 38.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -8.8) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A549 (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0635× (z -9.2) |
| [[C32 (line)]] | wt | 26.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.102× (z -9.5) |
| [[HCT15 (line)]] | alt | 26.4 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.161× (z -10.9) |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.102× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -8.7) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SK-MEL-2 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.168× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 56.1 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0894× (z -8.6) |
| [[A-172 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLGALT1]] | +0.69 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[RNF4]] | +0.66 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[WDR5]] | +0.66 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[SLC25A39]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[RNPS1]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SKP2]] | +0.64 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[BLTP2]] | +0.64 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[ENOPH1]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[GPAT4]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[SHANK3]] | +0.61 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[WRNIP1]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PEX5]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.61 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[AKAP9]] | -0.61 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[RSF1]] | -0.60 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[SEC62]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.59 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[CCDC186]] | -0.59 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[SMDT1]] | -0.58 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[UPF3B]] | -0.58 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[GIHCG]] | -0.57 | -0.68 / -0.46 | both halves | 2e-05 |  |
| [[LINC02307]] | -0.57 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[ZC3H6]] | -0.57 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[DCTN6]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VASH1]] | B | VASH1 activity raises TATDN2's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 1.48× lower at baseline in the lines without VASH1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[HDAC6]] | B | HDAC6 activity lowers TATDN2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.3, -19.3); signed map (-42.5, -13.5). **Vector** length 80.2, 14.6% of its response variance represented; |z| ≥ 3 in 856 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.6 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.6 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -5.5 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.2 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.7 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -2.8 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | TatD DNase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:10,248,023-10,281,218 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0218 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93075](https://www.uniprot.org/uniprotkb/Q93075) (3'-5' RNA nuclease TATDN2):

> Mg(2+)-dependent 3'RNA exonuclease and endonuclease that resolves R-loops via specific degradation of R-loop RNA structure. Shows no activity against D-loop and minimal activity against the RNA strand of an RNA-DNA hybrid duplex oligomer. Has no 3' or 5' exonuclease activity, no uracil glycosylase activity, and no 5' flap endonuclease activity on DNA substrates. May have a role in maintaining genomic stability through its role in R-loop resolution.

**Summary**, from NCBI Gene [9797](https://www.ncbi.nlm.nih.gov/gene/9797):

> Predicted to enable exonuclease activity and metal ion binding activity. Predicted to be located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28988) · Entrez [9797](https://www.ncbi.nlm.nih.gov/gene/9797) · UniProt [Q93075](https://www.uniprot.org/uniprotkb/Q93075) · Ensembl [ENSG00000157014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157014)

## Data

Gene col 8035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8035); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8035]; `tensor/DDL_lfc|DDL_z.npy` [8035]; `embed/gene_vectors.npy` [8035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8035 or target_col == 8035). Every well: [[TATDN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TATDN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
