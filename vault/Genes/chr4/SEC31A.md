---
symbol: "SEC31A"
type: "gene"
col: 6211
ensembl_id: "ENSG00000138674"
name: "SEC31 homolog A, COPII component"
location: "4q21.22"
module: 56
arm: "+"
pooled_cpm: 430.38
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SEC31A

*SEC31 homolog A, COPII component* — 4q21.22

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.698× (z -8.8, q 7e-16, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPB1]] (+0.86, fdr 7e-06), [[KDELR2]] (+0.86, fdr 7e-06), [[PDXDC1]] (+0.84, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GALNT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 1.46× | +3.4 | 0.36 | 28/49 (A498, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 1.42× | +3.2 | 0.45 | 23/48 (HS-578T, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6211.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.698×** | -8.8 | 7e-16 | 30/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.609×** | -8.3 | 4e-14 | 36/48 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.608×** | -8.0 | 3e-13 | 37/45 (SNU-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.746×** | -7.2 | 9e-11 | 39/48 (Hs 766T, SW 900, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -6.9 | 5e-10 | 33/49 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.680×** | -6.7 | 2e-09 | 32/49 (CFPAC-1, AsPC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.673×** | -6.6 | 3e-09 | 32/44 (SNU-1, LoVo, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.684×** | -6.6 | 3e-09 | 35/48 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.687×** | -6.5 | 5e-09 | 32/48 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -6.4 | 7e-09 | 39/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.699×** | -6.2 | 3e-08 | 35/48 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.709×** | -6.0 | 1e-07 | 38/48 (SW 900, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.702×** | -5.9 | 2e-07 | 36/47 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.720×** | -5.7 | 5e-07 | 39/48 (hTERT-HPNE, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.735×** | -5.1 | 1e-05 | 36/48 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.816×** | -5.0 | 2e-05 | 25/48 (NCI-H1573, hTERT-HPNE, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.751×** | -4.6 | 1e-04 | 36/47 (C32, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.805×** | -3.8 | 0.005 | 31/48 (HepG2/C3A, AsPC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -3.6 | 0.010 | 26/48 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.676×** | -3.5 | 0.010 | 29/49 (Hs 766T, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.832×** | -3.2 | 0.033 | 22/48 (A549, BT-474, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.833×** | -3.2 | 0.033 | 22/48 (LS 180, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 583 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -15.0) |
| [[SW 900 (line)]] | alt | 595 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -13.1) |
| [[hTERT-HPNE (line)]] | wt | 595 | 0 | 11 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.411× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 591 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -10.4) |
| [[LoVo (line)]] | wt | 591 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 688 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -13.2) |
| [[HOP62 (line)]] | alt | 558 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -14.4) |
| [[A549 (line)]] | wt | 389 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -16.7) |
| [[HS-578T (line)]] | alt | 486 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -13.1) |
| [[HT-29 (line)]] | alt | 533 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 603 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -18.8) |
| [[HCT15 (line)]] | alt | 606 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 662 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.449× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 519 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 437 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.452× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.611× (z -10.0) |
| [[SNU-423 (line)]] | alt | 238 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.541× (z -9.2) |
| [[A-172 (line)]] | wt | 437 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.533× (z -10.1) |
| [[H4 (line)]] | wt | 598 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 547 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.604× (z -9.6) |
| [[SNU-1 (line)]] | wt | 364 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 310 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.563× (z -9.1) |
| [[A498 (line)]] | wt | 525 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -10.9) |
| [[CHP-212 (line)]] | wt | 451 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 380 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -13.1) |
| [[J82 (line)]] | alt | 386 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.641× (z -9.2) |
| [[KATO III (line)]] | alt | 442 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H2030 (line)]] | alt | 357 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 301 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.452× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 831 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.4) |
| [[SW1417 (line)]] | alt | 352 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.638× (z -9.3) |
| [[AN3 CA (line)]] | alt | 315 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 270 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 291 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 503 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 354 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 226 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 437 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 419 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 314 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 447 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 333 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 332 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 359 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 463 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 366 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPB1]] | +0.86 | +0.90 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 678 |
| [[KDELR2]] | +0.86 | +0.87 / +0.81 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDXDC1]] | +0.84 | +0.84 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[TMEM263]] | +0.82 | +0.85 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SEC24D]] | +0.82 | +0.83 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_PROTEIN_SECRETION; STRING 994 |
| [[COPA]] | +0.82 | +0.83 / +0.79 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 704 |
| [[COG6]] | +0.81 | +0.83 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SRP54]] | +0.80 | +0.83 / +0.74 | both halves | 7e-06 |  |
| [[PDXDC2P]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.79 | +0.83 / +0.75 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.79 | +0.81 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 567 |
| [[NDEL1]] | +0.79 | +0.79 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT3]] | B | GALNT3 activity raises SEC31A's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.23× lower at baseline in the lines without GALNT3 | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[AGR2]] | B | AGR2 activity raises SEC31A's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.28× lower at baseline in the lines without AGR2 | 0.044 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.885). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, -33.8); signed map (-51.1, 10.9). **Vector** length 136, 57.8% of its response variance represented; |z| ≥ 3 in 1,208 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *COPI-dependent Golgi-to-ER retrograde traffic* (reactome, mean cos +0.75 to 9); *COPI-mediated anterograde transport* (reactome, mean cos +0.75 to 9); *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.73 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +4.2 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.9 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.6 | -6.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.6 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.0 | -6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -8.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | SEC31 homolog A, COPII component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.22 — chr4:82,818,509-82,901,166 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0905, ABP125, ABP130; previously SEC31L1 |
| Gene groups (HGNC) | WD repeat domain containing; Coat protein complex II |
| Hallmark sets | PROTEIN_SECRETION, UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 18 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; XBP1(S) activates chaperone genes; IRE1alpha activates chaperones |
| Matched by | ensembl_id |

**Function**, from UniProt [O94979](https://www.uniprot.org/uniprotkb/O94979) (Protein transport protein Sec31A):

> Component of the coat protein complex II (COPII) which promotes the formation of transport vesicles from the endoplasmic reticulum (ER). The coat has two main functions, the physical deformation of the endoplasmic reticulum membrane into vesicles and the selection of cargo molecules (By similarity).

**Summary**, from NCBI Gene [22872](https://www.ncbi.nlm.nih.gov/gene/22872):

> The protein encoded by this gene shares similarity with the yeast Sec31 protein, and is a component of the outer layer of the coat protein complex II (COPII). The encoded protein is involved in vesicle budding from the endoplasmic reticulum (ER) and contains multiple WD repeats near the N-terminus and a proline-rich region in the C-terminal half. It associates with the protein encoded by the SEC13 homolog, nuclear pore and COPII coat complex component (SEC13), and is required for ER-Golgi …

**Accessions** — [HGNC:17052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17052) · Entrez [22872](https://www.ncbi.nlm.nih.gov/gene/22872) · UniProt [O94979](https://www.uniprot.org/uniprotkb/O94979) · Ensembl [ENSG00000138674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138674)

## Data

Gene col 6211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6211); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6211]; `tensor/DDL_lfc|DDL_z.npy` [6211]; `embed/gene_vectors.npy` [6211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6211 or target_col == 6211). Every well: [[SEC31A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC31A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
