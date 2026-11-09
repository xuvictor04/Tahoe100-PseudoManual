---
symbol: "XRCC2"
type: "gene"
col: 12242
ensembl_id: "ENSG00000196584"
name: "X-ray repair cross complementing 2"
location: "7q36.1"
module: 6
arm: "+"
pooled_cpm: 19.52
n_lines_expressing: 48
n_dd_up: 35
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 13
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# XRCC2

*X-ray repair cross complementing 2* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (26 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.70× (z +15.2, q 0e+00, up in 26 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.35× (z +5.1, q 2e-05, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.566× (z -6.5, q 5e-08, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM8]] (+0.89, fdr 7e-06), [[MYBL2]] (+0.88, fdr 7e-06), [[CENPK]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 26 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 26 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **3.70×** | +15.2 | 0e+00 | 26/27 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **3.02×** | +13.3 | 6e-38 | 38/41 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.90×** | +11.9 | 3e-30 | 27/35 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.04×** | +8.6 | 1e-15 | 35/46 (A549, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **2.04×** | +8.6 | 1e-15 | 37/45 (A549, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.90×** | +7.4 | 1e-11 | 33/46 (SW480, HT-29, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.84×** | +7.1 | 1e-10 | 30/43 (SW480, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.68×** | +6.3 | 3e-08 | 29/45 (PANC-1, HT-29, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.57×** | +5.4 | 4e-06 | 24/46 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.1 | 2e-05 | 22/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.1 | 2e-05 | 26/45 (SW48, SW 900, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.35×** | +5.1 | 2e-05 | 22/46 (NCI-H1573, Panc 03.27, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~95% of this change | **1.53×** | +4.9 | 4e-05 | 23/43 (HT-29, CFPAC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.50×** | +4.9 | 4e-05 | 20/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.47×** | +4.6 | 1e-04 | 19/46 (HEC-1-A, SW480, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.003 | 17/46 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.007 | 16/45 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.021 | 7/46 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.024 | 15/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.024 | 10/45 (SW480, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.57×** | +2.8 | 0.079 | 7/44 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +2.8 | 0.087 | 9/45 (A-427, LoVo, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12242.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.566×** | -6.5 | 5e-08 | 29/46 (SNU-1, A498, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.516×** | -5.7 | 3e-06 | 26/46 (SW480, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.742×** | -5.1 | 6e-05 | 26/46 (COLO 205, HCT15, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.676×** | -4.7 | 3e-04 | 24/46 (A498, Panc 03.27, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.737×** | -4.2 | 0.002 | 21/46 (HEC-1-A, SNU-1, …) | two highest doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.716×** | -4.0 | 0.005 | 21/46 (A-427, C-33 A, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.539×** | -3.9 | 0.008 | 17/44 (H4, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.802×** | -3.8 | 0.010 | 20/44 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.732×** | -3.8 | 0.010 | 20/45 (KATO III, CFPAC-1, …) | two highest doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.750×** | -3.5 | 0.029 | 16/45 (NCI-H460, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.829×** | -3.2 | 0.066 | 22/46 (A498, LS 180, …) | all doses, flat | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.19 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 28.1 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.381× (z -8.6) |
| [[SW480 (line)]] | alt | 35.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -9.1) |
| [[A498 (line)]] | wt | 29.5 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.277× (z -11.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HEC-1-A (line)]] | alt | 45.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -9.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.465× (z -8.5) |
| [[LS 180 (line)]] | wt | 10.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.41× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | [[Selinexor (drug)]] 5 µM 0.206× (z -10.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0693× (z -19.6) |
| [[NCI-H460 (line)]] | wt | 18.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.07× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[A-172 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.306× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[C-33 A (line)]] | alt | 53.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[C32 (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.44× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[H4 (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0804× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.35× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H1792 (line)]] | alt | 5.95 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.3× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0610× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 44.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.5) |
| [[PANC-1 (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[A549 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM8]] | +0.89 | +0.87 / +0.89 | both halves | 7e-06 | STRING 574 |
| [[MYBL2]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CENPK]] | +0.88 | +0.89 / +0.91 | both halves | 7e-06 |  |
| [[POLE]] | +0.86 | +0.84 / +0.87 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 616 |
| [[CLSPN]] | +0.86 | +0.89 / +0.82 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[FANCD2]] | +0.86 | +0.82 / +0.88 | both halves | 7e-06 | same gene group; STRING 799 |
| [[WDR76]] | +0.86 | +0.86 / +0.86 | both halves | 7e-06 |  |
| [[GINS1]] | +0.86 | +0.86 / +0.82 | both halves | 7e-06 |  |
| [[MCM4]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 |  |
| [[VRK1]] | +0.85 | +0.86 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[CDC45]] | +0.85 | +0.86 / +0.85 | both halves | 7e-06 |  |
| [[FANCA]] | +0.84 | +0.87 / +0.85 | both halves | 7e-06 | same gene group; STRING 607 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 7, C 6. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises XRCC2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without E2F2 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises XRCC2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.58× lower at baseline in the lines without TCF19 | 0.013 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises XRCC2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.79× lower at baseline in the lines without CDC25A | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises XRCC2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.55× lower at baseline in the lines without E2F8 | 0.030 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers XRCC2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDCA7]] | B | CDCA7 activity raises XRCC2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without CDCA7 | 0.048 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises XRCC2's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without FAM111B | 0.056 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises XRCC2's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 3.24× lower at baseline in the lines without DSCC1 | 0.007 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[MYBL2]] | C | MYBL2 activity raises XRCC2's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.28× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[C21orf58]], [[CDC45]], [[CENPM]], [[SKA3]] | C | C21orf58, CDC45, CENPM, SKA3 activity raises XRCC2's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.48× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.061 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises XRCC2's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.62× lower at baseline in the lines without MCM10 | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises XRCC2's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.81× lower at baseline in the lines without E2F1, MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.884). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.5, -44.1); signed map (-37.6, -46.7). **Vector** length 129, 37.9% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.67 to 65); *DNA strand elongation* (reactome, mean cos +0.72 to 28); *DNA Replication* (reactome, mean cos +0.70 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | +6.5 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +6.4 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +6.0 | +11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.8 | +6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.3 | +3.3 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +3.2 |
|  | [[Oxaliplatin (drug)]] 0.5 µM |  | +2.5 | +2.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.4 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -5.1 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.9 | -6.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.7 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | -1.5 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.4 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.9 | -4.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | X-ray repair cross complementing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:152,644,776-152,676,193 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FANCU |
| Gene groups (HGNC) | FA complementation groups; RAD51 paralogs |
| Reactome | 18 pathways, smallest: Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA2/RAD51/RAD51C binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [O43543](https://www.uniprot.org/uniprotkb/O43543) (DNA repair protein XRCC2):

> Involved in the homologous recombination repair (HRR) pathway of double-stranded DNA, thought to repair chromosomal fragmentation, translocations and deletions. Part of the RAD51 paralog protein complex BCDX2 which acts in the BRCA1-BRCA2-dependent HR pathway. Upon DNA damage, BCDX2 acts downstream of BRCA2 recruitment and upstream of RAD51 recruitment. BCDX2 binds predominantly to the intersection of the four duplex arms of the Holliday junction and to junction of replication forks. The BCDX2 …

**Summary**, from NCBI Gene [7516](https://www.ncbi.nlm.nih.gov/gene/7516):

> This gene encodes a member of the RecA/Rad51-related protein family that participates in homologous recombination to maintain chromosome stability and repair DNA damage. This gene is involved in the repair of DNA double-strand breaks by homologous recombination and it functionally complements Chinese hamster irs1, a repair-deficient mutant that exhibits hypersensitivity to a number of different DNA-damaging agents. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12829) · Entrez [7516](https://www.ncbi.nlm.nih.gov/gene/7516) · UniProt [O43543](https://www.uniprot.org/uniprotkb/O43543) · Ensembl [ENSG00000196584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196584)

## Data

Gene col 12242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12242); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12242]; `tensor/DDL_lfc|DDL_z.npy` [12242]; `embed/gene_vectors.npy` [12242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12242 or target_col == 12242). Every well: [[XRCC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XRCC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
