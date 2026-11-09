---
symbol: "PRSS23"
type: "gene"
col: 7453
ensembl_id: "ENSG00000150687"
name: "serine protease 23"
location: "11q14.2"
module: 13
arm: "+"
pooled_cpm: 116.26
n_lines_expressing: 37
n_dd_up: 9
n_dd_down: 32
n_dd_up_clean: 6
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 28
direction_downstream: 25
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PRSS23

*serine protease 23* — 11q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.97× (z +7.9, q 1e-12, up in 24 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Carbamazepine (drug)]] 5 µM: 1.34× (z +3.6, q 0.057, up in 24 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.340× (z -13.2, q 9e-37, down in 32 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DKK3]] (+0.70, fdr 7e-06), [[SCUBE3]] (+0.69, fdr 7e-06), [[NMNAT2]] (+0.61, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[ME3]] → it (grade B ⚠); 25 go from it, the strongest it → [[MYO10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +7.9 | 1e-12 | 24/31 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.7 | 5e-12 | 24/36 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.057 | 24/34 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.057 | 20/35 (HS-578T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.4 | 0.057 | 16/32 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.057 | 17/35 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.057 | 18/35 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.057 | 17/35 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.060 | 14/35 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.12 | 18/36 (A-172, A498, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.28× | +3.0 | 0.14 | 17/36 (PANC-1, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7453.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.340×** | -13.2 | 9e-37 | 32/35 (Hs 766T, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.390×** | -11.5 | 4e-28 | 32/35 (Hs 766T, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.537×** | -10.7 | 2e-24 | 24/35 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.420×** | -10.6 | 6e-24 | 31/35 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.461×** | -9.4 | 5e-19 | 31/35 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.537×** | -7.6 | 3e-12 | 24/35 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.533×** | -7.2 | 3e-11 | 29/35 (HOP62, H4, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.562×** | -7.0 | 2e-10 | 30/35 (HOP62, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.570×** | -6.8 | 5e-10 | 25/35 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.350×** | -6.7 | 1e-09 | 25/33 (HOP62, SW 1088, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -4.7 | 1e-04 | 20/35 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.477×** | -4.7 | 1e-04 | 21/35 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.487×** | -4.6 | 2e-04 | 23/36 (KATO III, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.487×** | -4.6 | 2e-04 | 25/35 (LS 180, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.698×** | -4.4 | 4e-04 | 25/36 (H4, A-172, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.691×** | -4.3 | 5e-04 | 20/36 (SW 1088, A-172, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.702×** | -4.3 | 5e-04 | 18/35 (H4, Hs 766T, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 215 | 0 | 26 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.0) |
| [[HOP62 (line)]] | alt | 264 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -21.3) |
| [[A-172 (line)]] | wt | 491 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 172 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -20.4) |
| [[PANC-1 (line)]] | alt | 195 | 1 (1 ⚠) | 7 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.4) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -12.7) |
| [[HS-578T (line)]] | alt | 169 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +10.5) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.202× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 219 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -17.6) |
| [[SW 1088 (line)]] | alt | 747 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -13.3) |
| [[A549 (line)]] | wt | 96.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +13.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.243× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 95.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.4) |
| [[COLO 205 (line)]] | alt | 92.7 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.108× (z -15.1) |
| [[hTERT-HPNE (line)]] | wt | 321 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -9.8) |
| [[KATO III (line)]] | alt | 168 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -20.8) |
| [[LS 180 (line)]] | wt | 92.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -17.0) |
| [[SNU-1 (line)]] | wt | 186 | 1 | 3 | [[Homoharringtonine (drug)]] 0.05 µM 2.51× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.132× (z -18.8) |
| [[A498 (line)]] | wt | 48.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.3) |
| [[Hs 766T (line)]] | wt | 398 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -22.0) |
| [[LOX-IMVI (line)]] | wt | 97.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 82.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -12.5) |
| [[C32 (line)]] | wt | 64.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 65.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 142 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.3) |
| [[SNU-423 (line)]] | alt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +10.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -8.6) |
| [[SW 900 (line)]] | alt | 90.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.2) |
| [[SW1417 (line)]] | alt | 64.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -9.2) |
| [[A-427 (line)]] | wt | 8.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.77 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKK3]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SCUBE3]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[NMNAT2]] | +0.61 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ADAMTS6]] | +0.61 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[APCDD1L]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LINC00702]] | +0.60 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[DIRAS3]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[CD44]] | +0.59 | +0.54 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[HHIP]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[VEGFC]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[IGFBP7]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 | pathway: Post-translational protein phosphorylation |
| [[AK5]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 26, C 2. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ME3]] | B | ME3 activity raises PRSS23's level | lines that do not express ME3 (13) vs lines expressing it (37) | 3.03× lower at baseline in the lines without ME3 | 0.004 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[C12orf75-AS1]] | B | C12orf75-AS1 activity raises PRSS23's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 3.84× lower at baseline in the lines without C12orf75-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[COL7A1]] | B | COL7A1 activity raises PRSS23's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 3.07× lower at baseline in the lines without COL7A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[PTHLH]] | B | PTHLH activity raises PRSS23's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.96× lower at baseline in the lines without PTHLH | 0.007 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[INSYN2B]] | B | INSYN2B activity raises PRSS23's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.20× lower at baseline in the lines without INSYN2B | 0.009 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[DKK3]] | B | DKK3 activity raises PRSS23's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 3.30× lower at baseline in the lines without DKK3 | 0.011 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[SPOCK1]] | B | SPOCK1 activity raises PRSS23's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 2.69× lower at baseline in the lines without SPOCK1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[VEGFC]] | B | VEGFC activity raises PRSS23's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 2.88× lower at baseline in the lines without VEGFC | 0.015 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[COL5A1]] | B | COL5A1 activity raises PRSS23's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.18× lower at baseline in the lines without COL5A1 | 0.020 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[FRMD4A]] | B | FRMD4A activity raises PRSS23's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.60× lower at baseline in the lines without FRMD4A | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[SYTL2]] | B | SYTL2 activity raises PRSS23's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 2.95× lower at baseline in the lines without SYTL2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[BMPER]] | B | BMPER activity raises PRSS23's level | lines that do not express BMPER (21) vs lines expressing it (29) | 2.57× lower at baseline in the lines without BMPER | 0.035 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 23, C 2. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO10]] | B | PRSS23 activity raises MYO10's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.42× lower at baseline in the lines without PRSS23 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[TAGLN2]] | B | PRSS23 activity raises TAGLN2's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.91× lower at baseline in the lines without PRSS23 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[TGFBI]] | B | PRSS23 activity raises TGFBI's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 3.92× lower at baseline in the lines without PRSS23 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[PTHLH]] | B | PRSS23 activity raises PTHLH's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.52× lower at baseline in the lines without PRSS23 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[PTPN14]] | B | PRSS23 activity raises PTPN14's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 1.85× lower at baseline in the lines without PRSS23 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[INSYN2B]] | B | PRSS23 activity raises INSYN2B's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.31× lower at baseline in the lines without PRSS23 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | B | PRSS23 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 0.75× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| cells under [[Pentoxifylline (drug)]] 0.05 µM | B | PRSS23 activity raises the cells' numbers under Pentoxifylline 0.05 µM (protects the cells) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 0.82× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[ME3]] | B | PRSS23 activity raises ME3's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.13× lower at baseline in the lines without PRSS23 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[SMAD3]] | B | PRSS23 activity raises SMAD3's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.13× lower at baseline in the lines without PRSS23 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[EVA1A]] | B | PRSS23 activity raises EVA1A's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without PRSS23 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM | B | PRSS23 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 1.36× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.2, 18.1); signed map (23.0, 44.5). **Vector** length 117, 36.6% of its response variance represented; |z| ≥ 3 in 1,454 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen degradation* (reactome, mean cos +0.50 to 8); *Collagen chain trimerization* (reactome, mean cos +0.51 to 7); *Signaling by PDGF* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.4 | +2.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -6.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.6 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.4 | -2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.2 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | serine protease 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.2 — chr11:86,791,059-86,952,910 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPUVE, SIG13 |
| Gene groups (HGNC) | Serine proteases |
| Hallmark sets | COAGULATION, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

UniProt [O95084](https://www.uniprot.org/uniprotkb/O95084) carries no function annotation.

**Summary**, from NCBI Gene [11098](https://www.ncbi.nlm.nih.gov/gene/11098):

> This gene encodes a conserved member of the trypsin family of serine proteases. Mouse studies found a decrease of mRNA levels of this gene after ovulation was induced. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:14370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14370) · Entrez [11098](https://www.ncbi.nlm.nih.gov/gene/11098) · UniProt [O95084](https://www.uniprot.org/uniprotkb/O95084) · Ensembl [ENSG00000150687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150687)

## Data

Gene col 7453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7453); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7453]; `tensor/DDL_lfc|DDL_z.npy` [7453]; `embed/gene_vectors.npy` [7453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7453 or target_col == 7453). Every well: [[PRSS23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRSS23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
