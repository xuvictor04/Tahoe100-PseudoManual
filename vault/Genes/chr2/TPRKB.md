---
symbol: "TPRKB"
type: "gene"
col: 6836
ensembl_id: "ENSG00000144034"
name: "TP53RK binding protein"
location: "2p13.1"
module: 210
arm: "+"
pooled_cpm: 22.09
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# TPRKB

*TP53RK binding protein* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.11× (z +13.2, q 3e-37, up in 34 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.96× (z +11.9, q 2e-30, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.843× (z -4.3, q 0.007, down in 22 of 47 measured lines) ⚠ cell-cycle shift, explains ~0% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (HS-578T 0.0832×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Sonidegib (drug)]] 5 µM in 1 line (SHP-77 0.0815×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (H4 0.157×); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.222×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP43]] (+0.65, fdr 1e-05), [[ORC3]] (+0.64, fdr 7e-06), [[LSM3]] (+0.61, fdr 7e-06, ⚠ LSM3 in the vector space only through flagged drug-doses), [[PDZD11]] (+0.56, fdr 9e-05); moves opposite to [[MEMO1]] (-0.45, fdr 7e-05), [[SPECC1]] (-0.43, fdr 2e-04), [[GLIS2]] (-0.43, fdr 7e-04).
> It is in [[Module 210]], a single-armed module (tRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.11×** | +13.2 | 3e-37 | 34/43 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +11.9 | 2e-30 | 42/48 (A549, A498, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.92×** | +11.2 | 1e-26 | 29/36 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +9.8 | 2e-20 | 37/48 (NCI-H23, HOP62, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.68×** | +9.2 | 4e-18 | 40/48 (A549, MIA PaCa-2, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.74×** | +9.1 | 7e-18 | 23/39 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.66×** | +9.0 | 2e-17 | 38/48 (A549, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +5.9 | 3e-07 | 22/48 (SW 900, NCI-H2030, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +5.4 | 4e-06 | 22/47 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.35×** | +5.3 | 7e-06 | 23/44 (HS-578T, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.2 | 9e-06 | 21/43 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +4.6 | 2e-04 | 20/47 (A-172, SW1417, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.002 | 13/48 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.15× | +3.6 | 0.012 | 12/48 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +3.5 | 0.015 | 9/48 (NCI-H23, HS-578T, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.015 | 15/47 (NCI-H2030, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.016 | 10/44 (RKO, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.051 | 10/47 (Panc 03.27, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.073 | 15/48 (HOP62, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6836.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (HS-578T 0.0832×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Sonidegib (drug)]] 5 µM in 1 line (SHP-77 0.0815×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (H4 0.157×); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.222×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -4.3 | 0.007 | 22/47 (hTERT-HPNE, SNU-1, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.788×** | -4.2 | 0.007 | 18/48 (A-427, A498, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.839× | -3.1 | 0.33 | 15/48 (SW 1088, NCI-H460, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 25.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.19× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 21.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 25.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SHP-77 (line)]] | alt | 33.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Sonidegib (drug)]] 5 µM 0.0815× (z -10.0) |
| [[A-427 (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 25.5 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.157× (z -8.8) |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.222× (z -8.8) |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0832× (z -12.3) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -9.2) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 21.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW48 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0833× (z -10.3) ⚠ toxic |
| [[SW480 (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP43]] | +0.65 | +0.59 / +0.53 | both halves | 1e-05 | pathway: tRNA processing; STRING 799 |
| [[ORC3]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[LSM3]] ⚠ | +0.61 | +0.61 / +0.63 | both halves | 7e-06 | STRING 472; ⚠ in the vector space only through flagged drug-doses |
| [[PDZD11]] | +0.56 | +0.58 / +0.37 | both halves | 9e-05 |  |
| [[NUP214]] | +0.55 | +0.62 / +0.46 | both halves | 3e-05 | pathway: tRNA processing |
| [[VPS29]] | +0.54 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[POLR2C]] | +0.54 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[RTF2]] | +0.53 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[MAGOH]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ZW10]] | +0.53 | +0.57 / +0.37 | both halves | 7e-05 |  |
| [[RNF121]] | +0.52 | +0.54 / +0.28 | both halves | 3e-04 |  |
| [[GFM2]] | +0.52 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[ARL16]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEMO1]] | -0.45 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[SPECC1]] | -0.43 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[GLIS2]] | -0.43 | -0.51 / -0.21 | both halves | 7e-04 |  |
| [[ANKRD18A]] | -0.43 | -0.40 / -0.21 | both halves | 7e-04 |  |
| [[SLC12A2-DT]] | -0.42 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[RDX]] | -0.42 | -0.45 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[GYG1]] | -0.42 | -0.42 / -0.13 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-27.7, -48.0); signed map (-37.2, -31.4). **Vector** length 61.8, 9.63% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.9 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.8 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.9 | +9.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.1 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.2 | +0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -4.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | TP53RK binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:73,729,104-73,737,400 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-121, CGI121 |
| Gene groups (HGNC) | KEOPS complex |
| Hallmark sets | P53_PATHWAY |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3C4](https://www.uniprot.org/uniprotkb/Q9Y3C4) (EKC/KEOPS complex subunit TPRKB):

> Component of the EKC/KEOPS complex that is required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. The complex is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37. TPRKB acts as an allosteric effector that regulates the t(6)A activity of the complex. TPRKB is not required for tRNA modification.

**Summary**, from NCBI Gene [51002](https://www.ncbi.nlm.nih.gov/gene/51002):

> Enables protein kinase binding activity. Involved in tRNA threonylcarbamoyladenosine modification. Located in cytosol and nucleus. Part of EKC/KEOPS complex. Implicated in Galloway-Mowat syndrome 5. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24259) · Entrez [51002](https://www.ncbi.nlm.nih.gov/gene/51002) · UniProt [Q9Y3C4](https://www.uniprot.org/uniprotkb/Q9Y3C4) · Ensembl [ENSG00000144034](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144034)

## Data

Gene col 6836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6836); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6836]; `tensor/DDL_lfc|DDL_z.npy` [6836]; `embed/gene_vectors.npy` [6836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6836 or target_col == 6836). Every well: [[TPRKB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPRKB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
