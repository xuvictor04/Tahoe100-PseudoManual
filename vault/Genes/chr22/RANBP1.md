---
symbol: "RANBP1"
type: "gene"
col: 1826
ensembl_id: "ENSG00000099901"
name: "RAN binding protein 1"
location: "22q11.21"
module: 6
arm: "+"
pooled_cpm: 40.26
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RANBP1

*RAN binding protein 1* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 10.2× (z +18.0, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.57× (z +3.4, q 0.050, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (HT-29 13.9×, NCI-H1573 22.4×, PANC-1 11.9×, SW480 13.3×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 10.1×, NCI-H460 14.1×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.686× (z -3.9, q 0.047, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.232×); [[Selinexor (drug)]] 5 µM in 1 line (LOX-IMVI 0.220×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM3]] (+0.87, fdr 7e-06), [[CDCA7]] (+0.81, fdr 7e-06), [[MCM4]] (+0.81, fdr 7e-06); moves opposite to [[DNAJB2]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1826.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (HT-29 13.9×, NCI-H1573 22.4×, PANC-1 11.9×, SW480 13.3×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 10.1×, NCI-H460 14.1×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **10.2×** | +18.0 | 0e+00 | 45/45 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **8.08×** | +15.6 | 0e+00 | 39/39 (HT-29, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **7.14×** | +14.1 | 7e-43 | 44/44 (KATO III, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +6.2 | 8e-08 | 36/46 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **2.06×** | +5.4 | 8e-06 | 38/47 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.79×** | +4.5 | 5e-04 | 35/46 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.81×** | +4.4 | 8e-04 | 29/48 (MIA PaCa-2, SNU-423, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.61×** | +3.7 | 0.017 | 29/46 (SW 900, SW480, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.050 | 23/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.1 | 0.13 | 4/48 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.50× | +3.0 | 0.14 | 23/46 (MIA PaCa-2, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1826.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.232×); [[Selinexor (drug)]] 5 µM in 1 line (LOX-IMVI 0.220×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.686×** | -3.9 | 0.047 | 30/48 (NCI-H23, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.615×** | -3.8 | 0.047 | 33/48 (CHP-212, HT-29, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.80 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 21.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.7× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 20.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 16.2× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Selinexor (drug)]] 5 µM 0.220× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 25.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.88× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 47.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.12× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A498 (line)]] | wt | 61.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.01× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 19.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 23.9× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[CFPAC-1 (line)]] | alt | 31.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.74× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[H4 (line)]] | wt | 23.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.2× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 53.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.70× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 22.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.3× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 48.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.8× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 45.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HT-29 (line)]] | alt | 63.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.9× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.9× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 48.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.90× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 56.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.0× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 31.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.4× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LS 180 (line)]] | wt | 42.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.7× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 47.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.3× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 30.2× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 46.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 65.4 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +10.2) ⚠ cell-cycle shift, explains ~88% of this change | — |
| [[NCI-H460 (line)]] | wt | 24.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.0× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Panc 03.27 (line)]] | alt | 63.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.9× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 40.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.9× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 24.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.8× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 20.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.6× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW1417 (line)]] | alt | 65.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.83× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 47.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.3× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AsPC-1 (line)]] | alt | 19.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.81× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HCT15 (line)]] | alt | 40.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.0× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1573 (line)]] | alt | 19.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.4× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 53.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.55× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 66.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HepG2_C3A (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.17× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 53.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SHP-77 (line)]] | alt | 81.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.6× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW48 (line)]] | wt | 52.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.17× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AN3 CA (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3]] | +0.87 | +0.84 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CDCA7]] | +0.81 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[MCM4]] | +0.81 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 531 |
| [[POLA1]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[TFDP1]] | +0.80 | +0.85 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[CSE1L]] | +0.80 | +0.80 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 786 |
| [[FANCA]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.79 | +0.76 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[XRCC2]] | +0.77 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[TIMELESS]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[RAD54L]] | +0.77 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.77 | +0.75 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB2]] | -0.67 | -0.64 / -0.67 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises RANBP1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.72× lower at baseline in the lines without CDC25A | 0.039 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises RANBP1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.62× lower at baseline in the lines without TCF19 | 0.088 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises RANBP1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.03× lower at baseline in the lines without E2F1, MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.816). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.5, -42.2); signed map (-33.6, -44.6). **Vector** length 68.4, 22.4% of its response variance represented; |z| ≥ 3 in 745 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.64 to 28); *DNA Replication* (reactome, mean cos +0.62 to 40); *E2F G1/S* (control, mean cos +0.64 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | +2.4 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +2.2 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.2 | +4.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.6 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +3.4 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +1.4 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.3 | -0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -1.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.0 | +0.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -1.9 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | RAN binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,115,938-20,127,355 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HTF9A |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Hallmark sets | E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 7 pathways, smallest: Rev-mediated nuclear export of HIV RNA; Interactions of Rev with host cellular proteins; Host Interactions of HIV factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P43487](https://www.uniprot.org/uniprotkb/P43487) (Ran-specific GTPase-activating protein):

> Plays a role in RAN-dependent nucleocytoplasmic transport. Alleviates the TNPO1-dependent inhibition of RAN GTPase activity and mediates the dissociation of RAN from proteins involved in transport into the nucleus (By similarity). Induces a conformation change in the complex formed by XPO1 and RAN that triggers the release of the nuclear export signal of cargo proteins. Promotes the disassembly of the complex formed by RAN and importin beta. Promotes dissociation of RAN from a complex with …

**Summary**, from NCBI Gene [5902](https://www.ncbi.nlm.nih.gov/gene/5902):

> This gene encodes a protein that forms a complex with Ras-related nuclear protein (Ran) and metabolizes guanoside triphosphate (GTP). This complex participates in the regulation of the cell cycle by controlling transport of proteins and nucleic acids into the nucleus. There are multiple pseudogenes for this gene on chromosomes 9, 12, 17, and X. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:9847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9847) · Entrez [5902](https://www.ncbi.nlm.nih.gov/gene/5902) · UniProt [P43487](https://www.uniprot.org/uniprotkb/P43487) · Ensembl [ENSG00000099901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099901)

## Data

Gene col 1826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1826); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1826]; `tensor/DDL_lfc|DDL_z.npy` [1826]; `embed/gene_vectors.npy` [1826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1826 or target_col == 1826). Every well: [[RANBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RANBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
