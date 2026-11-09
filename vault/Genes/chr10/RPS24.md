---
symbol: "RPS24"
type: "gene"
col: 6154
ensembl_id: "ENSG00000138326"
name: "ribosomal protein S24"
location: "10q22.3"
module: 131
arm: "+"
pooled_cpm: 329.67
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPS24

*ribosomal protein S24* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.63× (z +9.7, q 2e-19, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 15 lines (COLO 205 5.36×, A-427 4.19×, HT-29 4.25×, NCI-H1573 4.99×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.444× (z -9.7, q 2e-19, down in 45 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 14 lines (SNU-1 0.240×, C-33 A 0.247×, SW480 0.289×, RKO 0.336×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.190×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS25]] (+0.94, fdr 7e-06), [[RPL7A]] (+0.89, fdr 7e-06), [[RPL36A]] (+0.89, fdr 7e-06); moves opposite to [[MIS12]] (-0.71, fdr 7e-06), [[SLC35A4]] (-0.71, fdr 7e-06), [[FAM111A]] (-0.66, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RGS10]] → it (grade C ⚠); 1 goes from it, the strongest it → [[SEC24B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6154.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 15 lines (COLO 205 5.36×, A-427 4.19×, HT-29 4.25×, NCI-H1573 4.99×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.63×** | +9.7 | 2e-19 | 49/49 (COLO 205, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +7.8 | 1e-12 | 44/44 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.04×** | +6.0 | 4e-07 | 47/48 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +4.8 | 2e-04 | 42/45 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +4.0 | 0.007 | 5/50 (RKO, CHP-212, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.65×** | +3.8 | 0.016 | 42/47 (NCI-H1573, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.51× | +3.1 | 0.13 | 37/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.79× | +3.1 | 0.13 | 47/48 (C-33 A, SW 1088, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6154.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 14 lines (SNU-1 0.240×, C-33 A 0.247×, SW480 0.289×, RKO 0.336×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.190×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.444×** | -9.7 | 2e-19 | 45/48 (SNU-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.628×** | -3.9 | 0.023 | 37/48 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 339 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.2) |
| [[A-427 (line)]] | wt | 263 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -13.3) |
| [[A549 (line)]] | wt | 387 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 288 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.3) |
| [[Hs 766T (line)]] | wt | 324 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 403 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.9) |
| [[LoVo (line)]] | wt | 429 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.8) |
| [[LS 180 (line)]] | wt | 366 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 328 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 331 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.6) ⚠ cell-cycle shift, explains ~24% of this change | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 475 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 390 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.6) |
| [[RKO (line)]] | wt | 361 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.7) |
| [[SHP-77 (line)]] | alt | 120 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.1) |
| [[SNU-1 (line)]] | wt | 269 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.1) |
| [[SNU-423 (line)]] | alt | 456 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.61× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 286 | 2 (2 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 3.18× (z +9.0) ⚠ transcription drop | — |
| [[SW48 (line)]] | wt | 589 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.7) |
| [[SW480 (line)]] | alt | 423 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -13.6) |
| [[A-172 (line)]] | wt | 247 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 331 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +9.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 235 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.6) |
| [[C32 (line)]] | wt | 156 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 406 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -10.8) |
| [[COLO 205 (line)]] | alt | 200 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.36× (z +10.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 267 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 302 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 506 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.9) |
| [[HOP62 (line)]] | alt | 275 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 210 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +9.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 256 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 187 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +8.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 325 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 324 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 351 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 269 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 267 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 243 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -11.2) |
| [[PANC-1 (line)]] | alt | 461 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 231 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 293 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.0) |
| [[AN3 CA (line)]] | alt | 438 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 19 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS25]] | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL7A]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.89 | +0.85 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL27A]] | +0.89 | +0.87 / +0.86 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS21]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL11]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.88 | +0.83 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS23]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS20]] | +0.88 | +0.84 / +0.87 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL38]] | +0.88 | +0.75 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS12]] | -0.71 | -0.70 / -0.64 | both halves | 7e-06 |  |
| [[SLC35A4]] | -0.71 | -0.72 / -0.66 | both halves | 7e-06 |  |
| [[FAM111A]] | -0.66 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[ZNF268]] | -0.65 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[COQ7]] | -0.65 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.65 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[ZNF620]] | -0.64 | -0.70 / -0.47 | both halves | 2e-05 |  |
| [[SCAF1]] | -0.64 | -0.70 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS10]] | C | RGS10 activity raises RPS24's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.44× lower at baseline in the lines without RGS10 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEC24B]] | C | RPS24's natural level strengthens SEC24B's drug response | RPS24's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.40; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.885). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.9, -28.5); signed map (-61.7, -4.9). **Vector** length 95.3, 51.9% of its response variance represented; |z| ≥ 3 in 535 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.86 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.1 | +0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.9 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.3 | +0.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.3 — chr10:78,033,760-78,056,813 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S24, eS24 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62847](https://www.uniprot.org/uniprotkb/P62847) (Small ribosomal subunit protein eS24):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Required for processing of pre-rRNA and maturation of 40S ribosomal subunits. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA …

**Summary**, from NCBI Gene [6229](https://www.ncbi.nlm.nih.gov/gene/6229):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S24E family of ribosomal proteins. It is located in the cytoplasm. Multiple transcript variants encoding different isoforms have been found for this gene. As is typical for …

**Accessions** — [HGNC:10411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10411) · Entrez [6229](https://www.ncbi.nlm.nih.gov/gene/6229) · UniProt [P62847](https://www.uniprot.org/uniprotkb/P62847) · Ensembl [ENSG00000138326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138326)

## Data

Gene col 6154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6154); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6154]; `tensor/DDL_lfc|DDL_z.npy` [6154]; `embed/gene_vectors.npy` [6154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6154 or target_col == 6154). Every well: [[RPS24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
