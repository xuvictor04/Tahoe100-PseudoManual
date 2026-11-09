---
symbol: "GSS"
type: "gene"
col: 2053
ensembl_id: "ENSG00000100983"
name: "glutathione synthetase"
location: "20q11.22"
module: 16
arm: "+"
pooled_cpm: 18.85
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# GSS

*glutathione synthetase* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.06× (z +18.6, q 0e+00, up in 34 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.54× (z +7.2, q 1e-10, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.753× (z -4.7, q 0.001, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.102×; ⚠ cell-cycle shift, explains ~54% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (A-172 0.223×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.329×; ⚠ cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SHP-77 0.193×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.349×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNPO]] (+0.71, fdr 7e-06), [[GUF1]] (+0.70, fdr 7e-06), [[ANAPC13]] (+0.67, fdr 1e-05); moves opposite to [[RPS6KA5]] (-0.65, fdr 1e-05), [[CAMLG]] (-0.62, fdr 1e-05), [[RPL35A]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.06×** | +18.6 | 0e+00 | 34/38 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.99×** | +17.5 | 0e+00 | 25/26 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +13.3 | 8e-38 | 28/33 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.2 | 1e-10 | 32/47 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.52×** | +6.7 | 3e-09 | 29/47 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +6.1 | 1e-07 | 23/47 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.29×** | +6.0 | 2e-07 | 22/47 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.35×** | +5.0 | 4e-05 | 22/43 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.4 | 6e-04 | 12/47 (NCI-H23, HT-29, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.64×** | +4.3 | 9e-04 | 12/43 (BT-474, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 0.001 | 16/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +4.1 | 0.002 | 15/47 (A-427, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.002 | 11/47 (LOX-IMVI, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.28×** | +3.9 | 0.003 | 16/43 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.17× | +3.6 | 0.010 | 10/48 (A549, HCT15, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.20× | +3.0 | 0.091 | 5/47 (SW480, HEC-1-A, …) | top dose only | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.091 | 9/46 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2053.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.102×; ⚠ cell-cycle shift, explains ~54% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (A-172 0.223×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.329×; ⚠ cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SHP-77 0.193×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.349×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.753×** | -4.7 | 0.001 | 18/47 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.664× | -3.6 | 0.10 | 11/46 (A-427, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 32.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -19.2) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.349× (z -8.9) |
| [[A-172 (line)]] | wt | 17.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +8.9) ⚠ toxic; transcription drop | [[Hesperidin (drug)]] 5 µM 0.223× (z -10.1) |
| [[J82 (line)]] | alt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +10.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.46× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 33.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 13.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 13.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +8.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 64.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.41× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.77× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.193× (z -9.2) |
| [[SNU-423 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[GUF1]] | +0.70 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ANAPC13]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[GTF2H3]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[PIGO]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[CEP41]] | +0.65 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[GMFB]] | +0.64 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[SLC35A4]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[NEK9]] | +0.63 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ALG10B]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MRPS7]] | +0.62 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[DARS2]] | +0.62 | +0.63 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS6KA5]] | -0.65 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.62 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[RPL35A]] | -0.60 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SPSB3]] | -0.59 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ULK1]] | -0.59 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[RPLP2]] | -0.59 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[IFT20]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[RPL18]] ⚠ | -0.58 | -0.44 / -0.51 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[GNRH1]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[RPL37A]] ⚠ | -0.57 | -0.44 / -0.53 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MXD4]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RPS14]] | -0.57 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[RPL26]] | -0.57 | -0.46 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.7, -16.8); signed map (0.3, -36.5). **Vector** length 66.0, 10.9% of its response variance represented; |z| ≥ 3 in 763 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.0 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.6 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.1 | +4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.9 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -3.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | glutathione synthetase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,928,432-34,956,027 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ligases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 6 pathways, smallest: Glutathione synthesis and recycling; Metabolic disorders of biological oxidation enzymes; Glutathione conjugation |
| Matched by | ensembl_id |

**Function**, from UniProt [P48637](https://www.uniprot.org/uniprotkb/P48637) (Glutathione synthetase):

> Catalyzes the production of glutathione from gamma-glutamylcysteine and glycine in an ATP-dependent manner. Glutathione (gamma-glutamylcysteinylglycine, GSH) is the most abundant intracellular thiol in living aerobic cells and is required for numerous processes including the protection of cells against oxidative damage, amino acid transport, the detoxification of foreign compounds, the maintenance of protein sulfhydryl groups in a reduced state and acts as a cofactor for a number of enzymes. …

**Summary**, from NCBI Gene [2937](https://www.ncbi.nlm.nih.gov/gene/2937):

> Glutathione is important for a variety of biological functions, including protection of cells from oxidative damage by free radicals, detoxification of xenobiotics, and membrane transport. The protein encoded by this gene functions as a homodimer to catalyze the second step of glutathione biosynthesis, which is the ATP-dependent conversion of gamma-L-glutamyl-L-cysteine to glutathione. Defects in this gene are a cause of glutathione synthetase deficiency. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4624) · Entrez [2937](https://www.ncbi.nlm.nih.gov/gene/2937) · UniProt [P48637](https://www.uniprot.org/uniprotkb/P48637) · Ensembl [ENSG00000100983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100983)

## Data

Gene col 2053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2053); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2053]; `tensor/DDL_lfc|DDL_z.npy` [2053]; `embed/gene_vectors.npy` [2053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2053 or target_col == 2053). Every well: [[GSS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
