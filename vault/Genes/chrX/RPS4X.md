---
symbol: "RPS4X"
type: "gene"
col: 12515
ensembl_id: "ENSG00000198034"
name: "ribosomal protein S4 X-linked"
location: "Xq13.1"
module: 43
arm: "+"
pooled_cpm: 275.71
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS4X

*ribosomal protein S4 X-linked* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.31× (z +10.2, q 1e-21, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +4.8, q 2e-04, up in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 14 lines (LoVo 4.78×, COLO 205 6.31×, HCT15 4.46×, MIA PaCa-2 4.39×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 2.53×, AsPC-1 2.20×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.677× (z -4.8, q 0.001, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.242×, C-33 A 0.365×, RKO 0.428×, SW480 0.466×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL7]] (+0.93, fdr 7e-06), [[RPS20]] (+0.91, fdr 7e-06), [[RPL30]] (+0.91, fdr 7e-06, ⚠ RPL30 in the vector space only through flagged drug-doses), [[RPL13A]] (+0.90, fdr 7e-06); moves opposite to [[SLC35A4]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12515.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 14 lines (LoVo 4.78×, COLO 205 6.31×, HCT15 4.46×, MIA PaCa-2 4.39×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 2.53×, AsPC-1 2.20×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.31×** | +10.2 | 1e-21 | 49/49 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +8.1 | 1e-13 | 44/44 (MIA PaCa-2, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +6.0 | 5e-07 | 43/45 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.76×** | +4.9 | 1e-04 | 46/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.8 | 2e-04 | 38/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.014 | 35/50 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.56×** | +3.7 | 0.019 | 39/47 (COLO 205, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.3 | 0.061 | 40/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12515.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.242×, C-33 A 0.365×, RKO 0.428×, SW480 0.466×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.677×** | -4.8 | 0.001 | 38/48 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 231 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 420 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -8.5) |
| [[SW480 (line)]] | alt | 356 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -8.6) |
| [[A-172 (line)]] | wt | 125 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 443 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 314 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.61× (z +10.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 421 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -12.0) |
| [[HT-29 (line)]] | alt | 282 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +10.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 137 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 313 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +12.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 250 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 318 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +10.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 455 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.8) |
| [[SHP-77 (line)]] | alt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 493 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 257 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 189 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +9.3) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 182 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +8.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.31× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 199 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 320 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 188 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 280 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +9.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 261 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 162 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 201 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +9.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 233 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 369 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 224 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 388 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 247 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 276 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 270 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 313 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 257 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 243 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 426 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 252 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 591 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL7]] | +0.93 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPS20]] | +0.91 | +0.87 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL30]] ⚠ | +0.91 | +0.84 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL13A]] | +0.90 | +0.85 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPL19]] | +0.88 | +0.85 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL12]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RACK1]] | +0.86 | +0.87 / +0.89 | both halves | 7e-06 | STRING 999 |
| [[RPL11]] | +0.86 | +0.86 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL37]] ⚠ | +0.85 | +0.76 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 995; ⚠ in the vector space only through flagged drug-doses |
| [[RPL27A]] | +0.85 | +0.77 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[NACA]] ⚠ | +0.85 | +0.82 / +0.85 | both halves | 7e-06 | STRING 727; ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.85 | +0.81 / +0.86 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS12]] | +0.84 | +0.77 / +0.86 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL26]] | +0.84 | +0.81 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 996 |
| [[RPLP0]] | +0.84 | +0.80 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | -0.60 | -0.46 / -0.62 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.874). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.6, -29.5); signed map (-60.5, -6.2). **Vector** length 79.1, 41.0% of its response variance represented; |z| ≥ 3 in 488 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.81 to 34); *MYC targets v1* (hallmark, mean cos +0.68 to 17); *oxidative phosphorylation* (hallmark, mean cos +0.56 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[AZD-8055 (drug)]] 0.5 µM |  | +2.5 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | -0.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.2 | +1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +1.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +2.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.1 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +0.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.1 | -0.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.1 | +2.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S4 X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:72,255,679-72,277,248 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DXS306, CCG2, SCAR, SCR10, FLJ40595, RPS4, eS4 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62701](https://www.uniprot.org/uniprotkb/P62701) (Small ribosomal subunit protein eS4, X isoform):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [6191](https://www.ncbi.nlm.nih.gov/gene/6191):

> Cytoplasmic ribosomes, organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes ribosomal protein S4, a component of the 40S subunit. Ribosomal protein S4 is the only ribosomal protein known to be encoded by more than one gene, namely this gene and ribosomal protein S4, Y-linked (RPS4Y). The 2 isoforms encoded by these genes are …

**Accessions** — [HGNC:10424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10424) · Entrez [6191](https://www.ncbi.nlm.nih.gov/gene/6191) · UniProt [P62701](https://www.uniprot.org/uniprotkb/P62701) · Ensembl [ENSG00000198034](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198034)

## Data

Gene col 12515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12515); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12515]; `tensor/DDL_lfc|DDL_z.npy` [12515]; `embed/gene_vectors.npy` [12515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12515 or target_col == 12515). Every well: [[RPS4X — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS4X.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
