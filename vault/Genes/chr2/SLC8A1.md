---
symbol: "SLC8A1"
type: "gene"
col: 11359
ensembl_id: "ENSG00000183023"
name: "solute carrier family 8 member A1"
location: "2p22.1"
module: 13
arm: "+"
pooled_cpm: 60.79
n_lines_expressing: 24
n_dd_up: 15
n_dd_down: 42
n_dd_up_clean: 12
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 49
direction_downstream: 42
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SLC8A1

*solute carrier family 8 member A1* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.20× (z +16.4, q 0e+00, up in 9 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.612× (z -7.2, q 3e-10, down in 20 of 22 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APBB1IP]] (+0.68, fdr 7e-06), [[ABI3BP]] (+0.65, fdr 7e-06), [[GRIN2A]] (+0.63, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[NREP]] → it (grade B ⚠); 42 go from it, the strongest it → [[PAPSS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +16.4 | 0e+00 | 9/21 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +14.2 | 4e-43 | 7/22 (RPMI-7951, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +6.5 | 2e-08 | 9/22 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.1 | 1e-07 | 7/21 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.7 | 2e-06 | 3/22 (AN3 CA, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.1 | 4e-05 | 2/19 (NCI-H23, H4) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 4e-05 | 2/22 (RPMI-7951, SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.004 | 13/21 (A-172, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.011 | 9/22 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.011 | 3/22 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +3.5 | 0.023 | 0/20 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.045 | 7/22 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.074 | 4/22 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.074 | 10/21 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.090 | 3/22 (SNU-423, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11359.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.612×** | -7.2 | 3e-10 | 20/22 (LOX-IMVI, A-172, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -6.8 | 2e-09 | 15/22 (LOX-IMVI, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -6.6 | 8e-09 | 21/22 (LOX-IMVI, SNU-423, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.658×** | -6.2 | 1e-07 | 16/22 (SNU-423, A498, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.679×** | -5.7 | 1e-06 | 10/22 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.674×** | -5.6 | 2e-06 | 16/21 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.696×** | -5.3 | 8e-06 | 8/22 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.776×** | -5.3 | 1e-05 | 15/22 (SNU-423, J82, …) | top dose only | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.706×** | -5.1 | 2e-05 | 11/21 (H4, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.711×** | -5.0 | 3e-05 | 15/21 (HOP62, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.736×** | -4.5 | 3e-04 | 11/22 (A498, SNU-423, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.736×** | -4.5 | 3e-04 | 17/22 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.737×** | -4.5 | 3e-04 | 15/22 (LOX-IMVI, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.731×** | -4.4 | 4e-04 | 14/22 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.749×** | -4.3 | 8e-04 | 13/21 (SNU-423, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.749×** | -4.2 | 8e-04 | 7/22 (A498, A549, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.750×** | -4.2 | 8e-04 | 11/22 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.757×** | -4.1 | 0.001 | 13/22 (LOX-IMVI, HOP62, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 843 | 0 | 15 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -18.0) |
| [[HS-578T (line)]] | alt | 169 | 0 | 9 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -13.6) |
| [[A-172 (line)]] | wt | 282 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +14.9) | [[Bortezomib (drug)]] 0.05 µM 0.175× (z -11.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.239× (z -10.2) |
| [[PANC-1 (line)]] | alt | 36.5 | 2 (1 ⚠) | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.25× (z +9.3) | [[Bortezomib (drug)]] 0.05 µM 0.258× (z -10.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 171 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.246× (z -11.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.179× (z -10.2) |
| [[A498 (line)]] | wt | 84.5 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.160× (z -10.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.192× (z -9.7) |
| [[HOP62 (line)]] | alt | 43.8 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 0.239× (z -9.3) |
| [[J82 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.162× (z -12.3) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 76.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +25.0) | — |
| [[NCI-H460 (line)]] | wt | 93.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +15.7) | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0397× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0607× (z -9.4) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 25.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.78× (z +11.0) | — |
| [[SW 1088 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0657× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 285 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.92 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.85 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 207 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.24 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.47 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.85 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APBB1IP]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[ABI3BP]] | +0.65 | +0.70 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[GRIN2A]] | +0.63 | +0.69 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[COL5A1]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[PRR16]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[KIRREL3]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[ADGRB3]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[LINC01411]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ADAMTS16]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LINC01615]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[VEGFC]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ADAMTS6]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 3, C 46. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NREP]] | B | NREP activity raises SLC8A1's level | lines that do not express NREP (13) vs lines expressing it (37) | 4.71× lower at baseline in the lines without NREP | 0.013 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |
| [[PAPSS2]] | B | PAPSS2 activity raises SLC8A1's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 3.24× lower at baseline in the lines without PAPSS2 | 0.040 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[GXYLT2]] | B | GXYLT2 activity raises SLC8A1's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 3.21× lower at baseline in the lines without GXYLT2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[ADAMTS6]] | C | ADAMTS6 activity raises SLC8A1's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 4.95× lower at baseline in the lines without ADAMTS6 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[APBB1IP]] | C | APBB1IP activity raises SLC8A1's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 7.06× lower at baseline in the lines without APBB1IP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises SLC8A1's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 5.18× lower at baseline in the lines without TCF4 | 0.011 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[KCTD16]] | C | KCTD16 activity raises SLC8A1's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 5.13× lower at baseline in the lines without KCTD16 | 0.011 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |
| [[GLIS3]] | C | GLIS3 activity raises SLC8A1's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 4.33× lower at baseline in the lines without GLIS3 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO; co-absent with the target |
| [[ODAD2]] | C | ODAD2 activity raises SLC8A1's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 3.38× lower at baseline in the lines without ODAD2 | 0.015 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises SLC8A1's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 6.30× lower at baseline in the lines without ADAMTS12 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises SLC8A1's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 6.59× lower at baseline in the lines without MSC-AS1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises SLC8A1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 4.20× lower at baseline in the lines without COL15A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 7, C 35. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPSS2]] | B | SLC8A1 activity raises PAPSS2's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 3.06× lower at baseline in the lines without SLC8A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[KLF7]] | B | SLC8A1 activity raises KLF7's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 4.20× lower at baseline in the lines without SLC8A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[GXYLT2]] | B | SLC8A1 activity raises GXYLT2's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 2.57× lower at baseline in the lines without SLC8A1 | 0.054 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[NREP]] | B | SLC8A1 activity raises NREP's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 3.59× lower at baseline in the lines without SLC8A1 | 0.059 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[SORCS2]] | B | SLC8A1 activity raises SORCS2's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without SLC8A1 | 0.085 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[NR2F2-AS1]] | B | SLC8A1 activity raises NR2F2-AS1's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 2.92× lower at baseline in the lines without SLC8A1 | 0.088 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[SLC8A1-AS1]] | B | SLC8A1 activity raises SLC8A1-AS1's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without SLC8A1 | 0.091 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[GNB4]] | C | SLC8A1 activity raises GNB4's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 6.31× lower at baseline in the lines without SLC8A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |
| [[PDCD1LG2]] | C | SLC8A1 activity raises PDCD1LG2's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 3.12× lower at baseline in the lines without SLC8A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |
| [[ADAMTS12]] | C | SLC8A1 activity raises ADAMTS12's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 6.44× lower at baseline in the lines without SLC8A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |
| [[ARHGEF6]] | C | SLC8A1 activity raises ARHGEF6's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 3.49× lower at baseline in the lines without SLC8A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |
| [[TGFBI]] | C | SLC8A1 activity raises TGFBI's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 4.86× lower at baseline in the lines without SLC8A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.3, 18.9); signed map (28.7, 46.7). **Vector** length 97.1, 33.6% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective B3GALTL causes PpS* (reactome, mean cos +0.52 to 8); *O-glycosylation of TSR domain-containing proteins* (reactome, mean cos +0.52 to 8); *Diseases associated with O-glycosylation of proteins* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.8 | +2.8 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -4.3 | -5.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.4 | -4.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.1 | -5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 8 member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:40,097,270-40,611,053 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NCX1 |
| Gene groups (HGNC) | Solute carrier family 8 |
| Reactome | 11 pathways, smallest: Sodium/Calcium exchangers; Reduction of cytosolic Ca++ levels; Platelet calcium homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P32418](https://www.uniprot.org/uniprotkb/P32418) (Sodium/calcium exchanger 1):

> Mediates the exchange of one Ca(2+) ion against three to four Na(+) ions across the cell membrane, and thereby contributes to the regulation of cytoplasmic Ca(2+) levels and Ca(2+)-dependent cellular processes. Contributes to Ca(2+) transport during excitation-contraction coupling in muscle. In a first phase, voltage-gated channels mediate the rapid increase of cytoplasmic Ca(2+) levels due to release of Ca(2+) stores from the endoplasmic reticulum. SLC8A1 mediates the export of Ca(2+) from the …

**Summary**, from NCBI Gene [6546](https://www.ncbi.nlm.nih.gov/gene/6546):

> In cardiac myocytes, Ca(2+) concentrations alternate between high levels during contraction and low levels during relaxation. The increase in Ca(2+) concentration during contraction is primarily due to release of Ca(2+) from intracellular stores. However, some Ca(2+) also enters the cell through the sarcolemma (plasma membrane). During relaxation, Ca(2+) is sequestered within the intracellular stores. To prevent overloading of intracellular stores, the Ca(2+) that entered across the sarcolemma …

**Accessions** — [HGNC:11068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11068) · Entrez [6546](https://www.ncbi.nlm.nih.gov/gene/6546) · UniProt [P32418](https://www.uniprot.org/uniprotkb/P32418) · Ensembl [ENSG00000183023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183023)

## Data

Gene col 11359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11359); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11359]; `tensor/DDL_lfc|DDL_z.npy` [11359]; `embed/gene_vectors.npy` [11359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11359 or target_col == 11359). Every well: [[SLC8A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC8A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
