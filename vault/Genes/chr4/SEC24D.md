---
symbol: "SEC24D"
type: "gene"
col: 7469
ensembl_id: "ENSG00000150961"
name: "SEC24 homolog D, COPII component"
location: "4q26"
module: 56
arm: "+"
pooled_cpm: 197.53
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 29
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SEC24D

*SEC24 homolog D, COPII component* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 1.91× (z +4.4, q 0.005, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.333× (z -17.6, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPA]] (+0.88, fdr 7e-06), [[KDELR2]] (+0.86, fdr 7e-06), [[SEC13]] (+0.85, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SNHG18]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GFPT1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +4.4 | 0.005 | 31/48 (hTERT-HPNE, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.033 | 34/49 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.039 | 28/48 (PANC-1, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +3.6 | 0.039 | 30/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.60× | +3.2 | 0.14 | 25/45 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.21 | 24/48 (LS 180, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7469.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.333×** | -17.6 | 0e+00 | 46/48 (RPMI-7951, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.338×** | -14.2 | 1e-43 | 45/49 (NCI-H2347, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.350×** | -13.8 | 6e-41 | 40/48 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.338×** | -13.7 | 1e-40 | 40/44 (SNU-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.475×** | -9.5 | 2e-19 | 44/48 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.474×** | -9.4 | 4e-19 | 41/47 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.478×** | -9.3 | 8e-19 | 42/48 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.536×** | -8.2 | 2e-14 | 38/48 (A498, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.625×** | -8.1 | 5e-14 | 41/48 (A-172, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.555×** | -7.7 | 6e-13 | 37/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.532×** | -7.7 | 1e-12 | 35/45 (NCI-H2347, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.564×** | -7.5 | 3e-12 | 37/48 (A498, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.638×** | -7.2 | 2e-11 | 39/48 (SNU-423, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -6.5 | 3e-09 | 35/49 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.625×** | -6.2 | 2e-08 | 35/48 (A498, H4, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.617×** | -6.1 | 4e-08 | 35/48 (RKO, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.651×** | -5.2 | 6e-06 | 35/47 (A549, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.692×** | -4.7 | 7e-05 | 30/49 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.721×** | -4.3 | 4e-04 | 37/48 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.722×** | -4.3 | 4e-04 | 33/48 (A549, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 381 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -22.3) |
| [[hTERT-HPNE (line)]] | wt | 472 | 2 | 14 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 6.35× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -16.6) |
| [[RPMI-7951 (line)]] | alt | 375 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -29.3) |
| [[A-172 (line)]] | wt | 247 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -18.3) |
| [[HS-578T (line)]] | alt | 388 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -17.4) |
| [[A498 (line)]] | wt | 405 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -21.4) |
| [[H4 (line)]] | wt | 467 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.246× (z -17.0) |
| [[KATO III (line)]] | alt | 221 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 262 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -25.4) |
| [[NCI-H2347 (line)]] | alt | 339 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -23.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 184 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -25.8) |
| [[J82 (line)]] | alt | 160 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -18.1) |
| [[SW 900 (line)]] | alt | 274 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -11.5) |
| [[A549 (line)]] | wt | 153 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -18.1) |
| [[SNU-423 (line)]] | alt | 164 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -19.9) |
| [[CFPAC-1 (line)]] | alt | 192 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -15.4) |
| [[Hs 766T (line)]] | wt | 239 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -18.0) |
| [[LoVo (line)]] | wt | 238 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -12.5) |
| [[C32 (line)]] | wt | 175 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.183× (z -12.4) |
| [[HT-29 (line)]] | alt | 227 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 209 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 119 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 158 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -18.3) |
| [[RKO (line)]] | wt | 219 | 0 | 4 (2 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.208× (z -13.6) |
| [[SW 1088 (line)]] | alt | 566 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -12.2) |
| [[SW1417 (line)]] | alt | 145 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.2) |
| [[BT-474 (line)]] | alt | 107 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -10.6) |
| [[COLO 205 (line)]] | alt | 294 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.260× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 146 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -13.0) |
| [[SNU-1 (line)]] | wt | 238 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0526× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.291× (z -11.8) |
| [[SW48 (line)]] | wt | 210 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -10.1) |
| [[HCT15 (line)]] | alt | 264 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -13.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 68.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -20.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 234 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 81.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 86.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -9.0) |
| [[PANC-1 (line)]] | alt | 83.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.8) |
| [[SHP-77 (line)]] | alt | 57.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -9.4) |
| [[SW 1271 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0746× (z -12.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 111 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 166 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 193 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 83.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPA]] | +0.88 | +0.90 / +0.83 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[KDELR2]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 496 |
| [[SEC13]] | +0.85 | +0.88 / +0.79 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[COPB1]] | +0.84 | +0.88 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 659 |
| [[TMEM39A]] | +0.84 | +0.87 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[COG6]] | +0.84 | +0.86 / +0.78 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PGM3]] | +0.83 | +0.80 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[SEC23A]] | +0.83 | +0.85 / +0.77 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[SEC31A]] | +0.82 | +0.83 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_PROTEIN_SECRETION; STRING 994 |
| [[GMPPA]] | +0.82 | +0.81 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[EIF2AK3]] | +0.81 | +0.83 / +0.76 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.81 | +0.85 / +0.75 | both halves | 7e-06 | STRING 592 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG18]] | B | SNHG18 activity raises SEC24D's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.74× lower at baseline in the lines without SNHG18 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[MCTP2]] | B | MCTP2 activity raises SEC24D's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.56× lower at baseline in the lines without MCTP2 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GFPT1]] | C | SEC24D's natural level strengthens GFPT1's drug response | SEC24D's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.12; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.920). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, -33.2); signed map (-51.3, 10.2). **Vector** length 142, 60.3% of its response variance represented; |z| ≥ 3 in 1,567 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *COPI-dependent Golgi-to-ER retrograde traffic* (reactome, mean cos +0.75 to 9); *COPI-mediated anterograde transport* (reactome, mean cos +0.76 to 9); *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.75 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | -6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -0.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.7 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | -13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | -1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.7 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.6 | +2.2 |
|  | [[EX229 (drug)]] 0.5 µM |  | +3.5 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.3 | -9.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.8 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -7.5 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -7.0 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -7.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.0 | -5.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.2 | -4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -6.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SEC24 homolog D, COPII component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q26 — chr4:118,722,823-118,838,683 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0755 |
| Gene groups (HGNC) | Coat protein complex II |
| Hallmark sets | PROTEIN_SECRETION, ANDROGEN_RESPONSE |
| Reactome | 19 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; Cargo concentration in the ER; Regulation of cholesterol biosynthesis by SREBP (SREBF) |
| Matched by | ensembl_id |

**Function**, from UniProt [O94855](https://www.uniprot.org/uniprotkb/O94855) (Protein transport protein Sec24D):

> Component of the coat protein complex II (COPII) which promotes the formation of transport vesicles from the endoplasmic reticulum (ER). The coat has two main functions, the physical deformation of the endoplasmic reticulum membrane into vesicles and the selection of cargo molecules for their transport to the Golgi complex. Plays a central role in cargo selection within the COPII complex and together with SEC24C may have a different specificity compared to SEC24A and SEC24B. May more …

**Summary**, from NCBI Gene [9871](https://www.ncbi.nlm.nih.gov/gene/9871):

> The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. This gene product is implicated in the shaping of the vesicle, and also in cargo selection and concentration. Mutations in this gene have been associated with Cole-Carpenter syndrome, a disorder affecting bone …

**Accessions** — [HGNC:10706](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10706) · Entrez [9871](https://www.ncbi.nlm.nih.gov/gene/9871) · UniProt [O94855](https://www.uniprot.org/uniprotkb/O94855) · Ensembl [ENSG00000150961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150961)

## Data

Gene col 7469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7469); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7469]; `tensor/DDL_lfc|DDL_z.npy` [7469]; `embed/gene_vectors.npy` [7469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7469 or target_col == 7469). Every well: [[SEC24D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC24D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
