---
symbol: "IMPG2"
type: "gene"
col: 1309
ensembl_id: "ENSG00000081148"
name: "interphotoreceptor matrix proteoglycan 2"
location: "3q12.3"
module: 39
arm: "+"
pooled_cpm: 6.04
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# IMPG2

*interphotoreceptor matrix proteoglycan 2* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +7.8, q 4e-12, up in 26 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.331× (z -9.0, q 9e-17, down in 32 of 43 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.546× (z -4.7, q 2e-04, down in 18 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYOCOS]] (+0.84, fdr 7e-06), [[LINC01191]] (+0.84, fdr 7e-06), [[GARIN1A]] (+0.83, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF577]] → it (grade B ⚠); 8 go from it, the strongest it → [[LRGUK]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +7.8 | 4e-12 | 26/39 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.53×** | +7.6 | 7e-12 | 39/43 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.5 | 6e-06 | 21/43 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +5.0 | 8e-05 | 18/44 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.005 | 13/43 (A-427, HOP62, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.69×** | +3.9 | 0.008 | 11/41 (A-427, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1309.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.331×** | -9.0 | 9e-17 | 32/43 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.359×** | -8.4 | 2e-14 | 26/38 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.433×** | -6.8 | 2e-09 | 27/43 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.436×** | -6.8 | 2e-09 | 27/40 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.456×** | -6.2 | 8e-08 | 18/30 (NCI-H1573, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.494×** | -5.7 | 9e-07 | 23/42 (Hs 766T, NCI-H1573, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.534×** | -5.1 | 3e-05 | 23/43 (NCI-H1573, NCI-H1792, …) | two highest doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.546×** | -4.7 | 2e-04 | 18/40 (SNU-1, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.564×** | -4.7 | 2e-04 | 20/43 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.557×** | -4.5 | 5e-04 | 21/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.561×** | -4.4 | 6e-04 | 18/43 (H4, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.607×** | -4.1 | 0.002 | 20/38 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.597×** | -4.0 | 0.002 | 18/33 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.627×** | -3.4 | 0.023 | 15/41 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.456×** | -3.3 | 0.031 | 10/33 (BT-474, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Bexarotene (drug)]] 5 µM |  | **0.694×** | -3.0 | 0.098 | 9/43 (SW48, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.30 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0607× (z -12.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0575× (z -11.4) |
| [[A-427 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0684× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 3.19 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0534× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 5.89 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0383× (z -11.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.146× (z -10.4) ⚠ toxic |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0489× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 5.53 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0655× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 8.97 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0401× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 3.89 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.0453× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 8.90 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0536× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 7.27 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0801× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 4.85 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0648× (z -11.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYOCOS]] | +0.84 | +0.83 / +0.77 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.84 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.83 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.83 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.81 | +0.81 / +0.69 | both halves | 7e-06 |  |
| [[LINC01934]] | +0.80 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[MPP4]] | +0.78 | +0.82 / +0.64 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.78 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[USP50]] | +0.78 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[LINC02803]] | +0.77 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[TTC36]] | +0.77 | +0.73 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF577]] | B | ZNF577 activity raises IMPG2's level | lines that do not express ZNF577 (10) vs lines expressing it (40) | 2.04× lower at baseline in the lines without ZNF577 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZNF649, ZNF724, ENSG00000283201 |
| [[MPP4]] | C | MPP4 activity raises IMPG2's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without MPP4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRGUK]] | C | IMPG2 activity raises LRGUK's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 2.51× lower at baseline in the lines without IMPG2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent; its own permutation p |
| [[RN7SL76P]] | C | IMPG2 activity lowers RN7SL76P's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 1.59× higher at baseline in the lines without IMPG2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent; its own permutation p |
| [[EFCAB10]] | C | IMPG2 activity raises EFCAB10's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 1.23× lower at baseline in the lines without IMPG2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent; its own permutation p |
| [[SLC4A5]] | C | IMPG2 activity raises SLC4A5's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 2.93× lower at baseline in the lines without IMPG2 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent |
| [[ITGA2B]] | C | IMPG2 activity raises ITGA2B's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without IMPG2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent; its own permutation p |
| [[NEK11]] | C | IMPG2 activity raises NEK11's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 1.84× lower at baseline in the lines without IMPG2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent; its own permutation p |
| [[PILRA]] | C | IMPG2 activity raises PILRA's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without IMPG2 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent |
| [[YIPF7]] | C | IMPG2 activity raises YIPF7's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without IMPG2 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.863). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.7, -13.3); signed map (18.1, 8.1). **Vector** length 83.2, 16.1% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | +2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.0 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +5.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | -1.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.8 | +4.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.9 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.4 | -5.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.1 | -3.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | interphotoreceptor matrix proteoglycan 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.3 — chr3:101,222,546-101,320,575 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IPM200, RP56, SPACRCAN |
| Gene groups (HGNC) | SEA domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZV3](https://www.uniprot.org/uniprotkb/Q9BZV3) (Interphotoreceptor matrix proteoglycan 2):

> Chondroitin sulfate- and hyaluronan-binding proteoglycan involved in the organization of interphotoreceptor matrix; may participate in the maturation and maintenance of the light-sensitive photoreceptor outer segment. Binds heparin.

**Summary**, from NCBI Gene [50939](https://www.ncbi.nlm.nih.gov/gene/50939):

> The protein encoded by this gene binds chondroitin sulfate and hyaluronan and is a proteoglycan. The encoded protein plays a role in the organization of the interphotoreceptor matrix and may promote the growth and maintenance of the light-sensitive photoreceptor outer segment. Defects in this gene are a cause of retinitis pigmentosa type 56 and maculopathy, IMPG2-related.[provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:18362](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18362) · Entrez [50939](https://www.ncbi.nlm.nih.gov/gene/50939) · UniProt [Q9BZV3](https://www.uniprot.org/uniprotkb/Q9BZV3) · Ensembl [ENSG00000081148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081148)

## Data

Gene col 1309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1309); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1309]; `tensor/DDL_lfc|DDL_z.npy` [1309]; `embed/gene_vectors.npy` [1309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1309 or target_col == 1309). Every well: [[IMPG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IMPG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
