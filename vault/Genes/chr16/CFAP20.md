---
symbol: "CFAP20"
type: "gene"
col: 964
ensembl_id: "ENSG00000070761"
name: "cilia and flagella associated protein 20"
location: "16q21"
module: 18
arm: "-"
pooled_cpm: 18.0
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CFAP20

*cilia and flagella associated protein 20* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.36× (z +25.5, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.265×, SW1417 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.163×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.0755×); [[Fenofibrate (drug)]] 5 µM in 1 line (HepG2/C3A 0.132×); [[Hesperidin (drug)]] 0.05 µM in 1 line (AN3 CA 0.0778×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKBIE]] (+0.54, fdr 1e-05), [[CBX8]] (+0.54, fdr 1e-05), [[CCDC148]] (+0.53, fdr 9e-06); moves opposite to [[DAP3]] (-0.60, fdr 1e-05), [[ME2]] (-0.57, fdr 6e-05), [[UBE2K]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.36×** | +25.5 | 0e+00 | 47/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.80×** | +19.8 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.36×** | +18.0 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.85×** | +15.6 | 0e+00 | 45/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.84×** | +15.5 | 0e+00 | 47/47 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.72×** | +14.9 | 0e+00 | 45/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.65×** | +13.9 | 5e-42 | 42/47 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +13.8 | 2e-41 | 43/47 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.77×** | +13.6 | 2e-40 | 45/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.50×** | +13.6 | 3e-40 | 41/46 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.93×** | +9.4 | 3e-19 | 33/45 (NCI-H460, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +9.2 | 2e-18 | 37/48 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +8.6 | 4e-16 | 29/48 (J82, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.73×** | +8.1 | 2e-14 | 30/47 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.71×** | +8.0 | 5e-14 | 33/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.48×** | +7.1 | 5e-11 | 27/45 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.8 | 4e-05 | 25/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +4.1 | 8e-04 | 11/48 (A549, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.004 | 17/47 (NCI-H460, HOP62, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.060 | 12/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 964.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.265×, SW1417 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.163×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.0755×); [[Fenofibrate (drug)]] 5 µM in 1 line (HepG2/C3A 0.132×); [[Hesperidin (drug)]] 0.05 µM in 1 line (AN3 CA 0.0778×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.9 | 5e-04 | 5/48 (RPMI-7951, SW48, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.803× | -3.2 | 0.29 | 6/47 (HEC-1-A, A-172, …) | top dose only | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.811× | -3.1 | 0.29 | 10/47 (H4, J82, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.771× | -3.1 | 0.29 | 11/48 (H4, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.818× | -3.0 | 0.29 | 10/47 (NCI-H460, SW 1271, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.2 | 17 (13 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +19.3) | — |
| [[LoVo (line)]] | wt | 16.8 | 7 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +12.4) | — |
| [[SW480 (line)]] | alt | 21.4 | 7 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +13.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.2) | — |
| [[KATO III (line)]] | alt | 21.1 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 15.1 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +17.2) | — |
| [[A549 (line)]] | wt | 15.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +16.5) | — |
| [[HOP62 (line)]] | alt | 16.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +15.2) | — |
| [[J82 (line)]] | alt | 21.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 10.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +15.8) | — |
| [[SW1417 (line)]] | alt | 24.1 | 4 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.23× (z +11.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.16× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 17.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +13.5) | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 16.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 29.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.5) | — |
| [[C32 (line)]] | wt | 11.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +13.8) | — |
| [[CFPAC-1 (line)]] | alt | 18.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 13.1 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.90× (z +10.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.84× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 7.44 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +11.4) | — |
| [[RKO (line)]] | wt | 22.5 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.3) | — |
| [[SW48 (line)]] | wt | 20.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +9.3) | — |
| [[A-172 (line)]] | wt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.3) | — |
| [[A-427 (line)]] | wt | 18.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 39.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 23.8 | 0 | 1 | — | [[Hesperidin (drug)]] 0.05 µM 0.0778× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.95× (z +9.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[BT-474 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.22× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.132× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 9.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +11.0) | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0755× (z -11.0) |
| [[SNU-423 (line)]] | alt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIE]] | +0.54 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CBX8]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CCDC148]] | +0.53 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[SMAD7]] | +0.52 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[CDC14A]] | +0.52 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[RAB38]] | +0.51 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[C4orf33]] | +0.51 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[MYLIP]] | +0.50 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[FAM8A1]] | +0.50 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[NR1D1]] | +0.49 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[NUP62CL]] | +0.49 | +0.30 / +0.59 | both halves | 2e-04 |  |
| [[ILK]] | +0.49 | +0.40 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAP3]] | -0.60 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[ME2]] | -0.57 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[UBE2K]] | -0.57 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[USP45]] | -0.50 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[ELMOD3]] | -0.50 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[POLR3E]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ECPAS]] | -0.49 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[C1orf159]] | -0.49 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[TMEM161A]] | -0.49 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[NUTM2A-AS1]] | -0.49 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[UQCC1]] | -0.48 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[TANGO2]] | -0.48 | -0.59 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **-** arm (projection on the module's main direction -0.378). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-5.9, -33.7); signed map (44.2, 2.6). **Vector** length 61.9, 12.2% of its response variance represented; |z| ≥ 3 in 1,158 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.2 | +8.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | +2.7 | +4.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.0 | +13.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +4.8 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.4 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | +0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | +0.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:58,113,592-58,129,381 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GTL3, fSAP23; previously C16orf80 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6A4](https://www.uniprot.org/uniprotkb/Q9Y6A4) (Cilia- and flagella-associated protein 20):

> Cilium- and flagellum-specific protein that plays a role in axonemal structure organization and motility. Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating. Involved in the regulation of the size and morphology of cilia. Required for axonemal microtubules polyglutamylation.

**Summary**, from NCBI Gene [29105](https://www.ncbi.nlm.nih.gov/gene/29105):

> Enables RNA binding activity. Involved in several processes, including positive regulation of feeding behavior; protein polyglutamylation; and regulation of cilium beat frequency involved in ciliary motility. Located in microtubule cytoskeleton and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29523](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29523) · Entrez [29105](https://www.ncbi.nlm.nih.gov/gene/29105) · UniProt [Q9Y6A4](https://www.uniprot.org/uniprotkb/Q9Y6A4) · Ensembl [ENSG00000070761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070761)

## Data

Gene col 964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 964); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 964]; `tensor/DDL_lfc|DDL_z.npy` [964]; `embed/gene_vectors.npy` [964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 964 or target_col == 964). Every well: [[CFAP20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
