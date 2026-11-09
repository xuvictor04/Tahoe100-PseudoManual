---
symbol: "SPC24"
type: "gene"
col: 8457
ensembl_id: "ENSG00000161888"
name: "SPC24 component of NDC80 kinetochore complex"
location: "19p13.2"
module: 67
arm: "+"
pooled_cpm: 15.29
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 19
direction_downstream: 1
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# SPC24

*SPC24 component of NDC80 kinetochore complex* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +8.2, q 1e-13, up in 23 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change. The strongest without an alert is [[Gallic acid (hydrate) (drug)]] 0.05 µM: 1.32× (z +3.3, q 0.048, up in 15 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.449× (z -13.4, q 4e-38, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPC25]] (+0.91, fdr 7e-06), [[CENPK]] (+0.91, fdr 7e-06), [[MELK]] (+0.91, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CCHCR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.00×** | +8.2 | 1e-13 | 23/38 (A498, A-172, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **2.00×** | +7.9 | 7e-13 | 16/24 (SNU-423, A498, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.46×** | +4.3 | 0.003 | 19/43 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.43×** | +4.3 | 0.003 | 19/48 (RKO, A549, …) | two highest doses | position effect removed |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.27×** | +4.0 | 0.006 | 22/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.40×** | +3.8 | 0.010 | 14/46 (MIA PaCa-2, J82, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.25×** | +3.8 | 0.010 | 12/48 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.8 | 0.010 | 15/47 (LoVo, RKO, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~88% of this change | **1.36×** | +3.7 | 0.015 | 16/43 (NCI-H2347, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.048 | 15/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.31×** | +3.2 | 0.061 | 17/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +3.1 | 0.100 | 15/48 (LoVo, RKO, …) | two highest doses | position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.29×** | +3.0 | 0.100 | 12/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8457.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.449×** | -13.4 | 4e-38 | 41/46 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.406×** | -10.7 | 4e-24 | 41/47 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.564×** | -6.8 | 2e-09 | 32/47 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.685×** | -6.3 | 3e-08 | 25/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.498×** | -5.9 | 4e-07 | 28/48 (SW480, A-172, …) | two highest doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -5.8 | 5e-07 | 25/46 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.658×** | -4.8 | 1e-04 | 20/47 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -4.8 | 1e-04 | 26/47 (COLO 205, C32, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.763×** | -4.5 | 4e-04 | 22/48 (Hs 766T, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.676×** | -4.4 | 7e-04 | 20/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.778×** | -4.2 | 0.001 | 22/48 (SNU-1, Hs 766T, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.712×** | -4.0 | 0.003 | 20/46 (SNU-1, Hs 766T, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.728×** | -3.8 | 0.007 | 15/47 (A-172, KATO III, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.554×** | -3.7 | 0.011 | 14/45 (LoVo, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.561×** | -3.6 | 0.013 | 14/45 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.753×** | -3.4 | 0.026 | 7/48 (NCI-H2030, RKO, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.041 | 10/48 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.765×** | -3.2 | 0.046 | 18/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.773×** | -3.0 | 0.062 | 16/47 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.701×** | -3.0 | 0.068 | 10/48 (SW480, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.785×** | -2.9 | 0.092 | 14/47 (A-172, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.72 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.0 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.112× (z -11.3) |
| [[A-427 (line)]] | wt | 33.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -20.0) |
| [[H4 (line)]] | wt | 21.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0244× (z -14.0) |
| [[A498 (line)]] | wt | 20.2 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.217× (z -13.3) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.296× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 39.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.4) |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.5) |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.1) |
| [[LoVo (line)]] | wt | 7.80 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.250× (z -9.7) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[palbociclib (drug)]] 5 µM 0.0385× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.0) |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 2 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0404× (z -11.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0728× (z -9.1) |
| [[SW480 (line)]] | alt | 24.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -19.5) |
| [[A549 (line)]] | wt | 7.83 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.242× (z -8.7) ⚠ cell-cycle shift, explains ~77% of this change |
| [[HCT15 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.8) |
| [[J82 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.2) |
| [[KATO III (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 9.25 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.114× (z -9.5) |
| [[LS 180 (line)]] | wt | 9.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.153× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -10.2) |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -11.8) |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPC25]] | +0.91 | +0.93 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[CENPK]] | +0.91 | +0.92 / +0.87 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 685 |
| [[MELK]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[POLQ]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[BLM]] | +0.89 | +0.88 / +0.86 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[FANCB]] | +0.88 | +0.85 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[EXO1]] | +0.88 | +0.87 / +0.86 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[NCAPG2]] | +0.88 | +0.88 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[FANCI]] | +0.88 | +0.88 / +0.83 | both halves | 7e-06 |  |
| [[STIL]] | +0.88 | +0.85 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[ATAD2]] | +0.87 | +0.85 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[DTL]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 7, C 12. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises SPC24's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.42× lower at baseline in the lines without TCF19 | 0.012 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises SPC24's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.36× lower at baseline in the lines without CDC25A | 0.016 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises SPC24's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without FAM111B | 0.031 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises SPC24's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.08× lower at baseline in the lines without E2F8 | 0.049 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[GGH]] | B | GGH activity raises SPC24's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without GGH | 0.067 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises SPC24's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without E2F2 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity strengthens SPC24's drug response | lines that do not express TCF19 (5) vs lines expressing it (43) | the lines without TCF19 respond 0.24× as strongly (z diff +2.07); strongest at Idarubicin (hydrochloride) 5 µM: 1.61x vs 0.62x (z diff +5.5) | 0.081 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises SPC24's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without DSCC1 | 0.020 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises SPC24's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.69× lower at baseline in the lines without AURKB | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises SPC24's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.32× lower at baseline in the lines without MCM10 | 0.037 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises SPC24's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without PBK | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises SPC24's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.68× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCHCR1]] | C | SPC24's natural level strengthens CCHCR1's drug response | SPC24's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.30; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.891). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.4, -47.0); signed map (-39.8, -43.3). **Vector** length 118, 32.2% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.78 to 9); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.75 to 4); *Nucleosome assembly* (reactome, mean cos +0.75 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.8 | +3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | +3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +3.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +0.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.8 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.4 | -10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -13.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -6.3 | -6.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -5.6 | -6.8 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -4.0 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | SPC24 component of NDC80 kinetochore complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,131,520-11,155,807 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90806; previously SPBC24 |
| Gene groups (HGNC) | NDC80 kinetochore complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBT2](https://www.uniprot.org/uniprotkb/Q8NBT2) (Kinetochore protein Spc24):

> Acts as a component of the essential kinetochore-associated NDC80 complex, which is required for chromosome segregation and spindle checkpoint activity. Required for kinetochore integrity and the organization of stable microtubule binding sites in the outer plate of the kinetochore. The NDC80 complex synergistically enhances the affinity of the SKA1 complex for microtubules and may allow the NDC80 complex to track depolymerizing microtubules.

**Summary**, from NCBI Gene [147841](https://www.ncbi.nlm.nih.gov/gene/147841):

> Predicted to contribute to microtubule binding activity. Involved in attachment of spindle microtubules to kinetochore. Located in kinetochore; nucleolus; and nucleoplasm. Part of Ndc80 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26913) · Entrez [147841](https://www.ncbi.nlm.nih.gov/gene/147841) · UniProt [Q8NBT2](https://www.uniprot.org/uniprotkb/Q8NBT2) · Ensembl [ENSG00000161888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161888)

## Data

Gene col 8457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8457); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8457]; `tensor/DDL_lfc|DDL_z.npy` [8457]; `embed/gene_vectors.npy` [8457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8457 or target_col == 8457). Every well: [[SPC24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPC24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
