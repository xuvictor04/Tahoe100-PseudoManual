---
symbol: "MZT1"
type: "gene"
col: 12932
ensembl_id: "ENSG00000204899"
name: "mitotic spindle organizing protein 1"
location: "13q21.33"
module: 22
arm: "+"
pooled_cpm: 52.09
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# MZT1

*mitotic spindle organizing protein 1* — 13q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +15.1, q 0e+00, up in 47 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 1.26× (z +3.2, q 0.086, up in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (SW480 3.09×, NCI-H1573 4.42×, Panc 03.27 3.76×, HOP62 3.62×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 3.30×, HOP62 3.54×, NCI-H460 3.75×, A-172 3.37×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HOP62 3.34×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 2.41×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.779× (z -5.0, q 3e-04, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAD2L1]] (+0.80, fdr 7e-06), [[GPSM2]] (+0.77, fdr 7e-06), [[CIT]] (+0.76, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NEURL1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12932.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (SW480 3.09×, NCI-H1573 4.42×, Panc 03.27 3.76×, HOP62 3.62×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 3.30×, HOP62 3.54×, NCI-H460 3.75×, A-172 3.37×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HOP62 3.34×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 2.41×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.01×** | +15.1 | 0e+00 | 47/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.64×** | +13.3 | 1e-37 | 37/41 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.93×** | +8.6 | 1e-15 | 39/45 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~70% of this change | **1.56×** | +6.3 | 4e-08 | 39/48 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.37×** | +4.5 | 9e-04 | 26/48 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~74% of this change | **1.30×** | +3.6 | 0.028 | 21/47 (A-172, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.27×** | +3.4 | 0.051 | 22/47 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.26×** | +3.3 | 0.066 | 20/48 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.086 | 18/48 (HT-29, KATO III, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.51× | +3.1 | 0.13 | 13/36 (NCI-H2347, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12932.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.779×** | -5.0 | 3e-04 | 27/48 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.709×** | -4.6 | 0.001 | 28/48 (PANC-1, LS 180, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.734×** | -4.4 | 0.002 | 26/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.817×** | -4.1 | 0.006 | 24/48 (A498, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.756×** | -3.8 | 0.015 | 27/48 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Posaconazole (drug)]] 5 µM |  | **0.759×** | -3.8 | 0.015 | 26/48 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.771×** | -3.7 | 0.017 | 23/48 (A498, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.783×** | -3.5 | 0.035 | 25/48 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.799×** | -3.2 | 0.088 | 19/48 (A498, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.799× | -3.1 | 0.12 | 19/47 (C-33 A, NCI-H2030, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.859× | -3.1 | 0.12 | 22/48 (SNU-1, NCI-H1573, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.809× | -3.0 | 0.12 | 19/48 (A-172, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 61.2 | 0 | 6 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.492× (z -10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -10.3) |
| [[A-427 (line)]] | wt | 70.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -18.2) |
| [[CFPAC-1 (line)]] | alt | 29.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 54.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 48.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 22.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 37.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 58.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -12.2) |
| [[SNU-1 (line)]] | wt | 76.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.239× (z -9.9) |
| [[SW480 (line)]] | alt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -8.9) |
| [[C32 (line)]] | wt | 42.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 44.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0972× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 72.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 81.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HT-29 (line)]] | alt | 87.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.381× (z -8.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[LoVo (line)]] | wt | 49.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 45.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 51.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 53.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 63.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 37.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-423 (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAD2L1]] | +0.80 | +0.77 / +0.79 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 446 |
| [[GPSM2]] | +0.77 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[CIT]] | +0.76 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[CCNA2]] | +0.74 | +0.78 / +0.70 | both halves | 7e-06 | pathway: G2/M Transition |
| [[NEK2]] | +0.74 | +0.66 / +0.73 | both halves | 7e-06 | pathway: Centrosome maturation |
| [[CEP55]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[PBK]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[PRR11]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[KIFC1]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[BUB1]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[DLGAP5]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[DEPDC1B]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | B | NEURL1B activity raises MZT1's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.37× lower at baseline in the lines without NEURL1B | 0.083 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity lowers MZT1's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[SKA3]] | C | SKA3 activity raises MZT1's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.6, -56.0); signed map (-49.0, -40.2). **Vector** length 112, 33.1% of its response variance represented; |z| ≥ 3 in 858 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.55 to 60); *DREAM G2/M down* (control, mean cos +0.62 to 28); *E2F targets* (hallmark, mean cos +0.53 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.0 | +4.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.8 | +1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.8 | +0.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.8 | -0.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -7.0 | -4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | -6.6 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | mitotic spindle organizing protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q21.33 — chr13:72,708,367-72,727,629 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOC440145, FLJ21869, MGC150539, RP11-11C5.2, MOZART1; previously C13orf37 |
| Reactome | 9 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; Recruitment of NuMA to mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08AG7](https://www.uniprot.org/uniprotkb/Q08AG7) (Mitotic-spindle organizing protein 1):

> Required for the recruitment and the assembly of the gamma-tubulin ring complex (gTuRC) at the centrosome. The gTuRC regulates the minus-end nucleation of alpha-beta tubulin heterodimers that grow into microtubule protafilaments, a critical step in centrosome duplication and spindle formation.

**Summary**, from NCBI Gene [440145](https://www.ncbi.nlm.nih.gov/gene/440145):

> Involved in gamma-tubulin complex localization. Located in centrosome and spindle. Part of gamma-tubulin ring complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33830](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33830) · Entrez [440145](https://www.ncbi.nlm.nih.gov/gene/440145) · UniProt [Q08AG7](https://www.uniprot.org/uniprotkb/Q08AG7) · Ensembl [ENSG00000204899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204899)

## Data

Gene col 12932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12932); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12932]; `tensor/DDL_lfc|DDL_z.npy` [12932]; `embed/gene_vectors.npy` [12932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12932 or target_col == 12932). Every well: [[MZT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MZT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
