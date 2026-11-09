---
symbol: "CDCA3"
type: "gene"
col: 3253
ensembl_id: "ENSG00000111665"
name: "cell division cycle associated 3"
location: "12p13.31"
module: 67
arm: "+"
pooled_cpm: 9.72
n_lines_expressing: 47
n_dd_up: 15
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 8
direction_downstream: 77
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CDCA3

*cell division cycle associated 3* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.09× (z +6.9, q 3e-09, up in 12 of 20 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 0.05 µM: 1.44× (z +3.7, q 0.011, up in 13 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.376× (z -9.9, q 3e-20, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA8]] (+0.93, fdr 7e-06), [[TROAP]] (+0.92, fdr 7e-06), [[TACC3]] (+0.92, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NEURL1B]] → it (grade B ⚠); 77 go from it, the strongest it → [[DEPDC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3253.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.09×** | +6.9 | 3e-09 | 12/20 (PANC-1, J82, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.94×** | +6.7 | 5e-09 | 17/32 (A498, SW480, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.91×** | +6.5 | 1e-08 | 26/41 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.84×** | +5.9 | 4e-07 | 20/37 (LoVo, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.69×** | +5.3 | 1e-05 | 24/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.69×** | +5.3 | 1e-05 | 18/34 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.66×** | +5.0 | 6e-05 | 11/16 (A498, HEC-1-A, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.59×** | +4.7 | 2e-04 | 21/44 (NCI-H23, KATO III, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.38×** | +4.6 | 2e-04 | 21/45 (NCI-H23, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.53×** | +4.3 | 1e-03 | 17/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.44×** | +3.7 | 0.011 | 13/44 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.95×** | +3.4 | 0.036 | 11/38 (J82, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.081 | 8/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +3.1 | 0.081 | 12/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.081 | 9/44 (LS 180, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3253.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.376×** | -9.9 | 3e-20 | 25/41 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.471×** | -7.6 | 1e-11 | 30/43 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.597×** | -7.4 | 4e-11 | 30/43 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.549×** | -6.0 | 2e-07 | 27/45 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.584×** | -5.1 | 3e-05 | 24/42 (SNU-1, HOP62, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.590×** | -5.1 | 3e-05 | 21/43 (HEC-1-A, J82, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.604×** | -5.1 | 3e-05 | 20/43 (LOX-IMVI, A-172, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.629×** | -4.7 | 2e-04 | 21/43 (LS 180, A498, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.429×** | -4.2 | 0.001 | 18/41 (HEC-1-A, J82, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.681×** | -3.9 | 0.006 | 17/44 (A498, MIA PaCa-2, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.661×** | -3.9 | 0.006 | 11/44 (PANC-1, SNU-1, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.542×** | -3.8 | 0.007 | 13/45 (A-427, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.690×** | -3.7 | 0.008 | 18/44 (HEC-1-A, SW48, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -3.7 | 0.010 | 17/44 (NCI-H2030, LOX-IMVI, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.709×** | -3.5 | 0.020 | 11/44 (SNU-1, H4, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.703×** | -3.3 | 0.037 | 10/44 (SNU-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | **0.729×** | -3.2 | 0.048 | 14/43 (LOX-IMVI, SNU-1, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.741×** | -3.0 | 0.071 | 11/44 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.731×** | -3.0 | 0.072 | 10/43 (SW 1271, RPMI-7951, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.733×** | -3.0 | 0.075 | 11/43 (A-427, SW480, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.815×** | -2.9 | 0.083 | 15/45 (Hs 766T, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +1.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.4 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.140× (z -17.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.5) |
| [[LoVo (line)]] | wt | 5.77 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0809× (z -10.4) |
| [[LS 180 (line)]] | wt | 7.35 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.116× (z -11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.189× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 9.08 | 0 | 3 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0220× (z -15.3) ⚠ cell-cycle shift, explains ~61% of this change |
| [[H4 (line)]] | wt | 13.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0572× (z -9.3) ⚠ cell-cycle shift, explains ~88% of this change |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0454× (z -9.7) ⚠ cell-cycle shift, explains ~92% of this change |
| [[SW480 (line)]] | alt | 12.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0629× (z -16.8) |
| [[A-172 (line)]] | wt | 5.69 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.104× (z -9.4) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-427 (line)]] | wt | 33.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.124× (z -17.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 8.05 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.124× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0938× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.301× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 5.00 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0581× (z -12.4) |
| [[SW48 (line)]] | wt | 8.51 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0579× (z -8.6) ⚠ cell-cycle shift, explains ~88% of this change |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA8]] | +0.93 | +0.90 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 975 |
| [[TROAP]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | STRING 857 |
| [[TACC3]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 773 |
| [[KIF22]] | +0.91 | +0.89 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 833 |
| [[CIT]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[KIF2C]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 930 |
| [[AURKB]] | +0.89 | +0.90 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 933 |
| [[SPAG5]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 877 |
| [[KIFC1]] | +0.88 | +0.89 / +0.83 | both halves | 7e-06 | STRING 830 |
| [[CCNA2]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | STRING 940 |
| [[GTSE1]] | +0.88 | +0.82 / +0.89 | both halves | 7e-06 | STRING 816 |
| [[TTK]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | STRING 858 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | B | NEURL1B activity raises CDCA3's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without NEURL1B | 0.031 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[NDC80]] | C | NDC80 activity raises CDCA3's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without NDC80 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises CDCA3's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.23× lower at baseline in the lines without PBK | 0.026 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises CDCA3's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.09× lower at baseline in the lines without AURKB | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PIMREG]] | C | PIMREG activity raises CDCA3's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.60× lower at baseline in the lines without PIMREG | 0.029 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[FAM72D]] | C | FAM72D activity raises CDCA3's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.86× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; co-absent with the target; its own permutation p |
| [[C21orf58]] | C | C21orf58 activity raises CDCA3's level | lines that do not express C21orf58 (3) vs lines expressing it (47) | 3.19× lower at baseline in the lines without C21orf58 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises CDCA3's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.88× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 0, C 77. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DEPDC1]] | C | CDCA3, [[SPDL1]] activity raises DEPDC1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 4.05× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[NEURL1B]] | C | CDCA3 activity raises NEURL1B's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.81× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |
| [[CENPF]] | C | CDCA3, [[SPDL1]] activity raises CENPF's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.80× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[KIF18B]] | C | CDCA3 activity raises KIF18B's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.77× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p |
| [[PBK]] | C | CDCA3 activity raises PBK's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.73× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target |
| [[DLGAP5]] | C | CDCA3, [[SPDL1]] activity raises DLGAP5's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.68× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[TICRR]] | C | CDCA3 activity raises TICRR's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.65× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p |
| [[NDC80]] | C | CDCA3, [[SPDL1]] activity raises NDC80's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.45× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[FOXM1]] | C | CDCA3 activity raises FOXM1's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.40× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p |
| [[BUB1B]] | C | CDCA3, [[SPDL1]] activity raises BUB1B's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.34× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[GTSE1]] | C | CDCA3, [[SPDL1]] activity raises GTSE1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.33× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[SKA1]] | C | CDCA3 activity raises SKA1's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.29× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.911). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.6, -55.8); signed map (-49.1, -41.4). **Vector** length 110, 29.5% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.80 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.75 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.75 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +3.8 | +5.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | +3.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +3.2 | +4.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +3.1 | +6.5 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.9 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +1.6 | +3.7 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -6.4 | -7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.8 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -9.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | -4.2 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -3.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle associated 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,844,793-6,851,292 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TOME-1, GRCC8 |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99618](https://www.uniprot.org/uniprotkb/Q99618) (Cell division cycle-associated protein 3):

> F-box-like protein which is required for entry into mitosis. Acts by participating in E3 ligase complexes that mediate the ubiquitination and degradation of WEE1 kinase at G2/M phase (By similarity).

**Summary**, from NCBI Gene [83461](https://www.ncbi.nlm.nih.gov/gene/83461):

> Predicted to be involved in cell division and protein ubiquitination. Located in adherens junction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14624) · Entrez [83461](https://www.ncbi.nlm.nih.gov/gene/83461) · UniProt [Q99618](https://www.uniprot.org/uniprotkb/Q99618) · Ensembl [ENSG00000111665](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111665)

## Data

Gene col 3253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3253); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3253]; `tensor/DDL_lfc|DDL_z.npy` [3253]; `embed/gene_vectors.npy` [3253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3253 or target_col == 3253). Every well: [[CDCA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDCA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
