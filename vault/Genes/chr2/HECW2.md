---
symbol: "HECW2"
type: "gene"
col: 6171
ensembl_id: "ENSG00000138411"
name: "HECT, C2 and WW domain containing E3 ubiquitin protein ligase 2"
location: "2q32.3"
module: 121
arm: "+"
pooled_cpm: 19.84
n_lines_expressing: 29
n_dd_up: 29
n_dd_down: 12
n_dd_up_clean: 23
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 19
direction_downstream: 17
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# HECW2

*HECT, C2 and WW domain containing E3 ubiquitin protein ligase 2* — 2q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.69× (z +9.7, q 2e-19, up in 13 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.504× (z -9.0, q 2e-16, down in 18 of 27 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLRT2]] (+0.66, fdr 1e-05), [[IL1R1]] (+0.65, fdr 8e-06), [[THSD7A]] (+0.62, fdr 3e-05); moves opposite to [[TNFRSF11A]] (-0.45, fdr 2e-04), [[C1QL1]] (-0.45, fdr 4e-04).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TRPA1]] → it (grade B ⚠); 17 go from it, the strongest it → [[SNHG26]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +9.7 | 2e-19 | 13/27 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +8.4 | 1e-14 | 10/27 (C-33 A, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.6 | 8e-09 | 14/27 (HOP62, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +6.5 | 1e-08 | 11/27 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 9e-04 | 8/27 (LOX-IMVI, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 0.001 | 10/26 (A-172, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.3 | 0.001 | 9/22 (NCI-H460, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.002 | 11/27 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.004 | 10/26 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.004 | 10/26 (HS-578T, A-172, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.004 | 11/27 (NCI-H460, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.004 | 9/27 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.37×** | +3.9 | 0.004 | 6/27 (HOP62, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.008 | 8/27 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.008 | 8/27 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.010 | 9/27 (HS-578T, BT-474, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.013 | 9/27 (PANC-1, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6171.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.504×** | -9.0 | 2e-16 | 18/27 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.600×** | -6.7 | 6e-09 | 17/27 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.612×** | -6.4 | 2e-08 | 17/24 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.704×** | -4.6 | 6e-04 | 16/27 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.714×** | -4.4 | 0.001 | 17/27 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.726×** | -4.2 | 0.003 | 13/27 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.042 | 9/27 (hTERT-HPNE, C-33 A, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.764×** | -3.4 | 0.042 | 5/27 (A549, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.772×** | -3.4 | 0.042 | 16/27 (NCI-H460, A-427, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.835× | -3.3 | 0.046 | 6/27 (H4, hTERT-HPNE, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.779×** | -3.3 | 0.054 | 7/27 (SW 1088, SW 1271, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.784×** | -3.2 | 0.063 | 9/27 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.628×** | -3.2 | 0.063 | 11/25 (PANC-1, A-427, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 71.9 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -18.9) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 75.7 | 2 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 7.19× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 40.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.333× (z -9.2) |
| [[SHP-77 (line)]] | alt | 75.2 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.192× (z -13.5) |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.161× (z -8.7) |
| [[A-172 (line)]] | wt | 13.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 19.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0851× (z -15.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 10.7 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.141× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 4.97 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0669× (z -10.2) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -14.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 6.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0816× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 86.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.235× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~76% of this change |
| [[SW 900 (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 80.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.37 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLRT2]] | +0.66 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[IL1R1]] | +0.65 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[THSD7A]] | +0.62 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[ZNF804A]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TEX41]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ARHGAP24]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[LINC00824]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[EBF1]] | +0.58 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[MGST1]] | +0.57 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[TBX18]] | +0.57 | +0.48 / +0.35 | both halves | 1e-04 |  |
| [[CACNA2D1]] | +0.56 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[NLGN4Y]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF11A]] | -0.45 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[C1QL1]] | -0.45 | -0.45 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 3, C 16. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPA1]] | B | TRPA1 activity strengthens HECW2's drug response | lines that do not express TRPA1 (12) vs lines expressing it (15) | the lines without TRPA1 respond 0.86× as strongly (z diff +0.13); strongest at Belinostat 5 µM: 0.75x vs 0.40x (z diff +3.6) | 0.036 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; target measured in part of the lines; both ways; artifact flags |
| [[SLC7A2]] | B | SLC7A2 activity raises HECW2's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.99× lower at baseline in the lines without SLC7A2 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[CARD18]] | B | CARD18 activity raises HECW2's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 3.84× lower at baseline in the lines without CARD18 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10 |
| [[TRPA1]] | C | TRPA1 activity raises HECW2's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 4.78× lower at baseline in the lines without TRPA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[ANTXR1]] | C | ANTXR1 activity raises HECW2's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 4.28× lower at baseline in the lines without ANTXR1 | 0.011 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804; co-absent with the target |
| [[ZEB2]] | C | ZEB2 activity raises HECW2's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 4.60× lower at baseline in the lines without ZEB2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[GLIS1]] | C | GLIS1 activity raises HECW2's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 3.81× lower at baseline in the lines without GLIS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |
| [[EPHA5-AS1]] | C | EPHA5-AS1 activity raises HECW2's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 4.55× lower at baseline in the lines without EPHA5-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[DCLK2]] | C | DCLK2 activity raises HECW2's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 4.84× lower at baseline in the lines without DCLK2 | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises HECW2's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 4.39× lower at baseline in the lines without PAPPA | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[ZNF804A]] | C | ZNF804A activity raises HECW2's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 4.22× lower at baseline in the lines without ZNF804A | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA; co-absent with the target |
| [[TBX18]] | C | TBX18 activity raises HECW2's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 2.49× lower at baseline in the lines without TBX18 | 0.063 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 7, C 10. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG26]] | B | HECW2 activity raises SNHG26's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 2.45× lower at baseline in the lines without HECW2 | 0.010 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041 |
| [[STXBP5]] | B | HECW2 activity raises STXBP5's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 1.41× lower at baseline in the lines without HECW2 | 0.033 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041 |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | HECW2 activity raises the cells' numbers under Minodronic acid 0.5 µM (protects the cells) | lines that do not express HECW2 (21) vs lines expressing it (27) | the lines without HECW2: 0.84× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041 |
| [[STEAP1B]] | B | HECW2 activity raises STEAP1B's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 1.79× lower at baseline in the lines without HECW2 | 0.058 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | HECW2 activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express HECW2 (21) vs lines expressing it (27) | the lines without HECW2: 0.88× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041 |
| [[SPRY3]] | B | HECW2 activity raises SPRY3's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 1.25× lower at baseline in the lines without HECW2 | 0.078 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041 |
| cells under [[Ixazomib (drug)]] 0.05 µM | B | HECW2 activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express HECW2 (21) vs lines expressing it (27) | the lines without HECW2: 1.31× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041 |
| [[ANTXR1]] | C | HECW2 activity raises ANTXR1's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 5.63× lower at baseline in the lines without HECW2 | 0.003 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041; co-absent with the target |
| [[DCLK2]] | C | HECW2 activity raises DCLK2's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 5.88× lower at baseline in the lines without HECW2 | 0.004 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041; co-absent with the target |
| [[GLIS1]] | C | HECW2 activity raises GLIS1's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 3.72× lower at baseline in the lines without HECW2 | 0.017 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041; co-absent with the target |
| [[BNC2]] | C | HECW2 activity raises BNC2's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 6.21× lower at baseline in the lines without HECW2 | 0.047 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041; co-absent with the target |
| [[RAB31]] | C | HECW2 activity raises RAB31's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 5.82× lower at baseline in the lines without HECW2 | 0.059 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.9, 24.8); signed map (42.6, 26.8). **Vector** length 76.4, 19.2% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.0 | -0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.8 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.2 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +6.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -0.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.8 | -9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -6.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | +0.7 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | HECT, C2 and WW domain containing E3 ubiquitin protein ligase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.3 — chr2:196,189,099-196,593,684 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1301, NEDL2 |
| Gene groups (HGNC) | C2 domain containing; Nedd4 family E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2P5](https://www.uniprot.org/uniprotkb/Q9P2P5) (E3 ubiquitin-protein ligase HECW2):

> E3 ubiquitin-protein ligase that mediates ubiquitination of TP73. Acts to stabilize TP73 and enhance activation of transcription by TP73. Involved in the regulation of mitotic metaphase/anaphase transition.

**Summary**, from NCBI Gene [57520](https://www.ncbi.nlm.nih.gov/gene/57520):

> This gene encodes a member of a family of E3 ubiquitin ligases which plays an important role in the proliferation, migration and differentiation of neural crest cells as a regulator of glial cell line-derived neurotrophic factor (GDNF)/Ret signaling. This gene also plays an important role in angiogenesis through stabilization of endothelial cell-to-cell junctions as a regulator of angiomotin-like 1 stability. The encoded protein contains an N-terminal calcium/lipid-binding (C2) domain involved …

**Accessions** — [HGNC:29853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29853) · Entrez [57520](https://www.ncbi.nlm.nih.gov/gene/57520) · UniProt [Q9P2P5](https://www.uniprot.org/uniprotkb/Q9P2P5) · Ensembl [ENSG00000138411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138411)

## Data

Gene col 6171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6171); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6171]; `tensor/DDL_lfc|DDL_z.npy` [6171]; `embed/gene_vectors.npy` [6171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6171 or target_col == 6171). Every well: [[HECW2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HECW2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
