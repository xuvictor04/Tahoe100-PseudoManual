---
symbol: "CDCA4"
type: "gene"
col: 10003
ensembl_id: "ENSG00000170779"
name: "cell division cycle associated 4"
location: "14q32.33"
module: 67
arm: "+"
pooled_cpm: 17.15
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CDCA4

*cell division cycle associated 4* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.14× (z +6.8, q 6e-09, up in 8 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.89× (z +4.9, q 7e-05, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.546× (z -8.6, q 3e-15, down in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.673× (z -8.5, q 7e-15, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF18B]] (+0.81, fdr 7e-06), [[UBE2T]] (+0.78, fdr 7e-06), [[BLM]] (+0.77, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +6.8 | 6e-09 | 8/48 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.02×** | +5.4 | 2e-05 | 20/48 (NCI-H2030, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +5.2 | 4e-05 | 17/43 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.40×** | +5.1 | 6e-05 | 21/47 (PANC-1, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.40×** | +5.0 | 6e-05 | 19/47 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +4.9 | 7e-05 | 22/46 (NCI-H2030, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **1.38×** | +4.8 | 1e-04 | 21/45 (A549, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.37×** | +4.7 | 2e-04 | 17/45 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.37×** | +4.7 | 2e-04 | 12/48 (LoVo, NCI-H1792, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.33×** | +4.3 | 0.001 | 18/47 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.18× | +3.6 | 0.018 | 6/48 (SW480, LS 180, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.4 | 0.035 | 10/48 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.043 | 6/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.047 | 11/45 (PANC-1, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.24×** | +3.2 | 0.057 | 12/39 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.057 | 6/48 (Hs 766T, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10003.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.546×** | -8.6 | 3e-15 | 34/47 (LOX-IMVI, SK-MEL-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.673×** | -8.5 | 7e-15 | 31/46 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.698×** | -7.7 | 3e-12 | 25/48 (A-427, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.604×** | -7.6 | 4e-12 | 28/47 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.661×** | -6.3 | 4e-08 | 25/47 (RPMI-7951, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.664×** | -6.2 | 6e-08 | 21/47 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -6.0 | 2e-07 | 24/47 (C32, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.676×** | -5.7 | 8e-07 | 22/46 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -4.8 | 8e-05 | 20/47 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.738×** | -4.6 | 2e-04 | 18/48 (COLO 205, A498, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.741×** | -4.4 | 7e-04 | 16/46 (J82, HOP62, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.679×** | -4.1 | 0.002 | 19/48 (A-427, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.780×** | -3.8 | 0.007 | 14/48 (CHP-212, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.6 | 0.013 | 17/46 (RKO, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.797×** | -3.4 | 0.022 | 12/46 (A498, A-172, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.860× | -3.2 | 0.039 | 12/48 (SHP-77, A549, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.804×** | -3.2 | 0.044 | 12/46 (NCI-H23, RKO, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.869× | -3.0 | 0.070 | 13/48 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.874× | -2.9 | 0.097 | 9/48 (J82, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 37.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.6) |
| [[RKO (line)]] | wt | 44.6 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 29.0 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.135× (z -19.2) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.309× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -10.2) |
| [[SW480 (line)]] | alt | 20.4 | 1 (1 ⚠) | 2 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.30× (z +9.5) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -10.3) |
| [[HOP62 (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 15.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -16.8) |
| [[SW48 (line)]] | wt | 27.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.7) |
| [[A549 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 17.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.131× (z -10.7) |
| [[H4 (line)]] | wt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0766× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.217× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LS 180 (line)]] | wt | 10.00 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.257× (z -9.4) ⚠ cell-cycle shift, explains ~73% of this change |
| [[NCI-H2030 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.319× (z -9.0) ⚠ cell-cycle shift, explains ~73% of this change |
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0956× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF18B]] | +0.81 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[UBE2T]] | +0.78 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[BLM]] | +0.77 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[ERCC6L]] | +0.76 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[AURKB]] | +0.76 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[STIL]] | +0.75 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[SPC24]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[RFWD3]] | +0.74 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[FBXO5]] | +0.74 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[KIFC1]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[CCNF]] | +0.73 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[RBL1]] | +0.73 | +0.68 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises CDCA4's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.14× lower at baseline in the lines without TCF19 | 0.016 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises CDCA4's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without CDC25A | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises CDCA4's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without E2F8 | 0.028 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[PIMREG]] | B | PIMREG activity raises CDCA4's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.90× lower at baseline in the lines without PIMREG | 0.043 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CDCA4's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without AURKB | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises CDCA4's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without MCM10 | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises CDCA4's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without PBK | 0.051 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDC45]], [[CENPM]], [[SKA3]] | C | CDC45, CENPM, SKA3 activity raises CDCA4's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.37× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[ZNF367]] | C | ZNF367 activity raises CDCA4's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 1.75× lower at baseline in the lines without ZNF367 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises CDCA4's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without CDCA3 | 0.095 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.5, -51.8); signed map (-44.4, -40.4). **Vector** length 108, 25.8% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.66 to 12); *G2/M checkpoint* (hallmark, mean cos +0.64 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.61 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +5.1 | +5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.1 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.7 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.8 | +3.3 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +1.8 | +3.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.7 | +1.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.3 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.1 | -0.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.1 | -8.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -5.6 | -7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -5.4 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle associated 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:105,009,573-105,021,083 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEI-3, TRIP-Br3, FLJ20764, Hepp |
| Gene groups (HGNC) | SERTA domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXL8](https://www.uniprot.org/uniprotkb/Q9BXL8) (Cell division cycle-associated protein 4):

> May participate in the regulation of cell proliferation through the E2F/RB pathway. May be involved in molecular regulation of hematopoietic stem cells and progenitor cell lineage commitment and differentiation (By similarity).

**Summary**, from NCBI Gene [55038](https://www.ncbi.nlm.nih.gov/gene/55038):

> This gene encodes a protein that belongs to the E2F family of transcription factors. This protein regulates E2F-dependent transcriptional activation and cell proliferation, mainly through the E2F/retinoblastoma protein pathway. It also functions in the regulation of JUN oncogene expression. This protein shows distinctive nuclear-mitotic apparatus distribution, it is involved in spindle organization from prometaphase, and may also play a role as a midzone factor involved in chromosome …

**Accessions** — [HGNC:14625](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14625) · Entrez [55038](https://www.ncbi.nlm.nih.gov/gene/55038) · UniProt [Q9BXL8](https://www.uniprot.org/uniprotkb/Q9BXL8) · Ensembl [ENSG00000170779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170779)

## Data

Gene col 10003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10003); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10003]; `tensor/DDL_lfc|DDL_z.npy` [10003]; `embed/gene_vectors.npy` [10003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10003 or target_col == 10003). Every well: [[CDCA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDCA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
