---
symbol: "MOB1A"
type: "gene"
col: 3607
ensembl_id: "ENSG00000114978"
name: "MOB kinase activator 1A"
location: "2p13.1"
module: 25
arm: "+"
pooled_cpm: 79.72
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# MOB1A

*MOB kinase activator 1A* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.83× (z +17.9, q 0e+00, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.61× (z +8.5, q 2e-15, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.800× (z -4.0, q 0.034, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~13% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.495×, NCI-H2347 0.572×; ⚠ cell-cycle shift, explains ~92% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.450×; ⚠ cell-cycle shift, explains ~7% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (SW48 0.355×; ⚠ cell-cycle shift, explains ~13% of this change); [[Crizotinib (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0868×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGRMC1]] (+0.77, fdr 7e-06), [[MMGT1]] (+0.77, fdr 7e-06), [[TMX1]] (+0.77, fdr 7e-06); moves opposite to [[SMIM26]] (-0.79, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[NSUN5P1-1]] (-0.73, fdr 7e-06), [[MARCHF9]] (-0.72, fdr 7e-06), [[EML2]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +17.9 | 0e+00 | 43/44 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +16.8 | 0e+00 | 46/49 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +12.2 | 7e-32 | 42/45 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +8.5 | 2e-15 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +7.7 | 1e-12 | 3/49 (C-33 A, NCI-H661, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +7.6 | 3e-12 | 37/49 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.7 | 1e-09 | 36/50 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.6 | 3e-09 | 40/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +6.1 | 6e-08 | 34/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +5.6 | 1e-06 | 34/48 (HEC-1-A, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.6 | 2e-04 | 26/47 (Hs 766T, A-172, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.5 | 3e-04 | 24/48 (SW1417, A-427, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +4.2 | 0.001 | 27/48 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +3.7 | 0.010 | 22/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.21×** | +3.4 | 0.025 | 23/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.081 | 16/48 (C32, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3607.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.495×, NCI-H2347 0.572×; ⚠ cell-cycle shift, explains ~92% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.450×; ⚠ cell-cycle shift, explains ~7% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (SW48 0.355×; ⚠ cell-cycle shift, explains ~13% of this change); [[Crizotinib (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0868×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.800×** | -4.0 | 0.034 | 24/48 (SW48, C32, …) | two highest doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.743× | -3.5 | 0.12 | 21/48 (SHP-77, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.2 | 0.18 | 17/48 (A-172, J82, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.18 | 16/48 (SW1417, H4, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.768× | -3.1 | 0.18 | 18/48 (KATO III, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 0.769× | -3.1 | 0.18 | 18/48 (HepG2/C3A, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 98.5 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +11.4) | — |
| [[A-427 (line)]] | wt | 115 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.72× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -10.9) ⚠ cell-cycle shift, explains ~92% of this change |
| [[C32 (line)]] | wt | 44.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.3) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[HOP62 (line)]] | alt | 83.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +14.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 49.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +10.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 66.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +11.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 100 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.3) | — |
| [[LoVo (line)]] | wt | 80.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 77.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 92.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 63.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.21× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -8.9) ⚠ cell-cycle shift, explains ~92% of this change |
| [[NCI-H460 (line)]] | wt | 71.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 100 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +15.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 96.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +12.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 88.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +15.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 79.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +14.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 56.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 76.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 59.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 54.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.17× (z +14.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 54.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 59.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 59.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 66.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +8.5) ⚠ toxic; transcription drop | [[Tucidinostat (drug)]] 0.5 µM 0.355× (z -8.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[AsPC-1 (line)]] | alt | 95.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +9.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 96.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 68.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +8.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 58.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 94.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 82.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 78.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 152 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 87.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 77.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 75.2 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.05 µM 0.0868× (z -8.5) |
| [[SW 900 (line)]] | alt | 56.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 99.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 91.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGRMC1]] | +0.77 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[MMGT1]] | +0.77 | +0.72 / +0.84 | both halves | 7e-06 |  |
| [[TMX1]] | +0.77 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.76 | +0.64 / +0.81 | both halves | 7e-06 |  |
| [[TWF1]] | +0.76 | +0.61 / +0.85 | both halves | 7e-06 |  |
| [[TARDBP]] | +0.76 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[EIF4G2]] | +0.75 | +0.61 / +0.79 | both halves | 7e-06 |  |
| [[DHFR]] | +0.74 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[PSME3]] | +0.74 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[RCN1]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[SUMO3]] | +0.73 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[CAPRIN1]] | +0.72 | +0.59 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | -0.79 | -0.73 / -0.78 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5P1-1]] | -0.73 | -0.58 / -0.77 | both halves | 7e-06 |  |
| [[MARCHF9]] | -0.72 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[NSUN5P2-1]] ⚠ | -0.72 | -0.53 / -0.77 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MTLN]] ⚠ | -0.71 | -0.53 / -0.70 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EML2]] | -0.70 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[TMEM258]] | -0.70 | -0.57 / -0.76 | both halves | 1e-05 |  |
| [[ARID3A]] | -0.70 | -0.48 / -0.73 | both halves | 2e-05 |  |
| [[RPL36AL]] ⚠ | -0.70 | -0.48 / -0.77 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPP21]] | -0.70 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[ZNF593]] | -0.70 | -0.52 / -0.79 | both halves | 1e-05 |  |
| [[RPL36]] | -0.69 | -0.55 / -0.75 | both halves | 1e-05 |  |
| [[C19orf81]] | -0.69 | -0.49 / -0.72 | both halves | 1e-05 |  |
| [[RPS26]] | -0.69 | -0.44 / -0.74 | both halves | 3e-05 |  |
| [[RBMX2]] | -0.68 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[MPHOSPH10]] | -0.68 | -0.53 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MOB1A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TNFRSF10A-DT]] | B | TNFRSF10A-DT activity raises MOB1A's level | lines that do not express TNFRSF10A-DT (11) vs lines expressing it (39) | 1.24× lower at baseline in the lines without TNFRSF10A-DT | 0.046 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, SLC16A5, ARHGEF16 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.778). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.9, -21.8); signed map (-18.0, -37.6). **Vector** length 134, 40.8% of its response variance represented; |z| ≥ 3 in 813 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +17.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +16.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.9 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +12.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.0 | +6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.2 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.6 | +2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +3.6 | +1.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | +3.5 | +2.2 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -6.1 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -4.9 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -4.9 | -4.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -4.2 | -2.0 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.9 | -3.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | MOB kinase activator 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,152,528-74,178,898 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10788, MOB1, FLJ11595, Mob4B, Mats1; previously C2orf6, MOBK1B, MOBKL1B |
| Gene groups (HGNC) | MOB kinase activators |
| Reactome | 1 pathways, smallest: Signaling by Hippo |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8S9](https://www.uniprot.org/uniprotkb/Q9H8S9) (MOB kinase activator 1A):

> Activator of LATS1/2 in the Hippo signaling pathway which plays a pivotal role in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein STK3/MST2 and STK4/MST1, in complex with its regulatory protein SAV1, phosphorylates and activates LATS1/2 in complex with its regulatory protein MOB1, which in turn phosphorylates and inactivates YAP1 oncoprotein and WWTR1/TAZ. Phosphorylation of YAP1 by …

**Summary**, from NCBI Gene [55233](https://www.ncbi.nlm.nih.gov/gene/55233):

> The protein encoded by this gene is a component of the Hippo signaling pathway, which controls organ size and tumor growth by enhancing apoptosis. Loss of the encoded protein results in cell proliferation and cancer formation. The encoded protein is also involved in the control of microtubule stability during cytokinesis. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:16015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16015) · Entrez [55233](https://www.ncbi.nlm.nih.gov/gene/55233) · UniProt [Q9H8S9](https://www.uniprot.org/uniprotkb/Q9H8S9) · Ensembl [ENSG00000114978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114978)

## Data

Gene col 3607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3607); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3607]; `tensor/DDL_lfc|DDL_z.npy` [3607]; `embed/gene_vectors.npy` [3607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3607 or target_col == 3607). Every well: [[MOB1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOB1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
