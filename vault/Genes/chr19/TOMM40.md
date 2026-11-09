---
symbol: "TOMM40"
type: "gene"
col: 5034
ensembl_id: "ENSG00000130204"
name: "translocase of outer mitochondrial membrane 40"
location: "19q13.32"
module: 36
arm: "+"
pooled_cpm: 29.19
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# TOMM40

*translocase of outer mitochondrial membrane 40* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (24 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.22× (z +13.5, q 2e-38, up in 42 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.65× (z +5.7, q 5e-07, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.554× (z -6.9, q 3e-09, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAD3A]] (+0.80, fdr 7e-06), [[URB2]] (+0.74, fdr 7e-06), [[NOM1]] (+0.74, fdr 7e-06); moves opposite to [[CHMP2B]] (-0.66, fdr 7e-06), [[ABCA5]] (-0.65, fdr 9e-06), [[OSER1-DT]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 24 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5034.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **3.22×** | +13.5 | 2e-38 | 42/44 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **3.28×** | +13.2 | 3e-37 | 35/37 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.75×** | +10.8 | 9e-25 | 38/41 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.62×** | +7.8 | 8e-13 | 36/47 (A549, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.95×** | +7.7 | 1e-12 | 41/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.95×** | +7.7 | 1e-12 | 36/48 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.95×** | +7.4 | 1e-11 | 38/46 (HOP62, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.89×** | +7.3 | 1e-11 | 41/48 (HOP62, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.90×** | +7.1 | 8e-11 | 37/46 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.83×** | +7.0 | 2e-10 | 40/47 (AsPC-1, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.78×** | +6.2 | 4e-08 | 38/48 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.66×** | +5.8 | 3e-07 | 30/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +5.7 | 5e-07 | 30/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +5.2 | 9e-06 | 32/47 (HOP62, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.55×** | +5.0 | 2e-05 | 33/47 (A-172, HOP62, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.30×** | +5.0 | 2e-05 | 36/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.29×** | +5.0 | 2e-05 | 34/48 (NCI-H460, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +4.8 | 4e-05 | 30/45 (KATO III, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.19×** | +4.7 | 7e-05 | 27/46 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.17×** | +4.7 | 8e-05 | 31/46 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.69×** | +4.3 | 4e-04 | 26/48 (NCI-H23, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +4.2 | 6e-04 | 25/47 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.2 | 6e-04 | 27/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 7e-04 | 21/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.98×** | +4.1 | 8e-04 | 26/45 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.61×** | +3.9 | 0.002 | 22/48 (NCI-H460, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.009 | 20/46 (HOP62, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +3.4 | 0.013 | 21/48 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.554×** | -6.9 | 3e-09 | 34/47 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.640×** | -5.0 | 2e-04 | 32/47 (C-33 A, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.743×** | -4.9 | 2e-04 | 32/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.672×** | -4.1 | 0.005 | 23/48 (LoVo, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.791×** | -3.9 | 0.011 | 25/48 (A-427, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.556×** | -3.6 | 0.033 | 19/47 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.760× | -3.2 | 0.11 | 20/48 (SW 1271, HOP62, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.768× | -3.1 | 0.14 | 15/48 (KATO III, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.0 | 0.16 | 19/47 (A-427, RKO, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.74 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 72.4 | 6 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.94× (z +10.3) | [[Tucidinostat (drug)]] 0.5 µM 0.401× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 18.7 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.06× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 40.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[SW480 (line)]] | alt | 45.1 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 39.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.07× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 21.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[A549 (line)]] | wt | 27.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[KATO III (line)]] | alt | 36.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.33× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H460 (line)]] | wt | 16.4 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.68× (z +8.9) ⚠ unreliable plate only | — |
| [[Panc 03.27 (line)]] | alt | 27.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[A-172 (line)]] | wt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.44× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[HCT15 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.49× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[HEC-1-A (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[Hs 766T (line)]] | wt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.74× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[HT-29 (line)]] | alt | 34.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[J82 (line)]] | alt | 44.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[LS 180 (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H23 (line)]] | alt | 30.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +9.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[RKO (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.01× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[A498 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD3A]] | +0.80 | +0.75 / +0.79 | both halves | 7e-06 | STRING 521 |
| [[URB2]] | +0.74 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[NOM1]] | +0.74 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[WDR4]] | +0.73 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.73 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[UTP4]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.71 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[SLC25A10]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[EIF3B]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[CHID1]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[TBL3]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP2B]] | -0.66 | -0.61 / -0.59 | both halves | 7e-06 | pathway: Autophagy |
| [[ABCA5]] | -0.65 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[OSER1-DT]] | -0.61 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[LCA5]] | -0.60 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[COMMD3]] | -0.60 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[EIF1]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[YTHDC1]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises TOMM40's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without CDC25A | 0.072 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TOMM40's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.740). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-14.0, -35.2); signed map (-4.2, -47.3). **Vector** length 80.1, 22.6% of its response variance represented; |z| ≥ 3 in 1,240 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +7.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.7 | +4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +5.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.7 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.6 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | translocase of outer mitochondrial membrane 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:44,890,569-44,903,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEREC1, D19S1177E, C19orf1, TOM40, PER-EC1 |
| Gene groups (HGNC) | Translocase of outer mitochondrial membrane complex |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: PINK1-PRKN Mediated Mitophagy; Mitophagy; Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [O96008](https://www.uniprot.org/uniprotkb/O96008) (Mitochondrial import receptor subunit TOM40 homolog):

> Channel-forming protein that forms part of the translocase of the outer mitochondrial membrane (TOM) complex essential for the recognition and translocation of cytosolically synthesized mitochondrial preproteins. The TOM complex associates with the ion channel VDAC2 and PINK1 kinase at depolarized mitochondria, this interaction stabilizes PINK1 at the outer mitochondrial membrane and triggers downstream mitophagy by the recruitment of the E3 ubiquitin ligase PRKN. Plays a role in the assembly …

**Summary**, from NCBI Gene [10452](https://www.ncbi.nlm.nih.gov/gene/10452):

> The protein encoded by this gene is localized in the outer membrane of the mitochondria. It is the channel-forming subunit of the translocase of the mitochondrial outer membrane (TOM) complex that is essential for import of protein precursors into mitochondria. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:18001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18001) · Entrez [10452](https://www.ncbi.nlm.nih.gov/gene/10452) · UniProt [O96008](https://www.uniprot.org/uniprotkb/O96008) · Ensembl [ENSG00000130204](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130204)

## Data

Gene col 5034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5034); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5034]; `tensor/DDL_lfc|DDL_z.npy` [5034]; `embed/gene_vectors.npy` [5034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5034 or target_col == 5034). Every well: [[TOMM40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOMM40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
