---
symbol: "JAG2"
type: "gene"
col: 11590
ensembl_id: "ENSG00000184916"
name: "jagged canonical Notch ligand 2"
location: "14q32.33"
module: 132
arm: "+"
pooled_cpm: 9.39
n_lines_expressing: 40
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 10
direction_downstream: 24
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# JAG2

*jagged canonical Notch ligand 2* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.49× (z +5.0, q 4e-04, up in 15 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.373× (z -11.8, q 1e-29, down in 29 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDZD4]] (+0.68, fdr 7e-06), [[KLHL17]] (+0.68, fdr 1e-05), [[BMP8B]] (+0.66, fdr 3e-05); moves opposite to [[DECR1]] (-0.55, fdr 2e-04), [[C11orf58]] (-0.54, fdr 4e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[KIF26A]] → it (grade B ⚠); 24 go from it, the strongest it → [[PARD6G]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +5.0 | 4e-04 | 15/38 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +4.8 | 4e-04 | 5/13 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.006 | 9/37 (J82, CHP-212, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.1 | 0.007 | 11/29 (NCI-H1792, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.025 | 8/34 (SW 900, RKO, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.028 | 13/38 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.054 | 11/31 (LS 180, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.054 | 3/35 (MIA PaCa-2, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.057 | 6/36 (A-427, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11590.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.373×** | -11.8 | 1e-29 | 29/37 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.647×** | -7.7 | 3e-12 | 24/37 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.550×** | -7.5 | 1e-11 | 20/36 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.538×** | -7.3 | 3e-11 | 23/34 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.557×** | -7.3 | 3e-11 | 19/37 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.586×** | -6.7 | 2e-09 | 20/35 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.594×** | -6.5 | 5e-09 | 24/38 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.594×** | -6.5 | 5e-09 | 22/37 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.648×** | -5.4 | 3e-06 | 18/38 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.662×** | -5.2 | 1e-05 | 16/37 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.680×** | -4.8 | 7e-05 | 17/37 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -4.7 | 1e-04 | 18/36 (RKO, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.503×** | -4.5 | 3e-04 | 14/25 (SW48, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.778×** | -4.5 | 3e-04 | 16/38 (SW480, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -3.2 | 0.049 | 17/37 (RKO, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.838× | -3.1 | 0.060 | 16/38 (Hs 766T, A498, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.623×** | -3.1 | 0.064 | 8/35 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 64.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 26.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0961× (z -22.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0918× (z -16.0) |
| [[PANC-1 (line)]] | alt | 6.14 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.183× (z -9.4) |
| [[RKO (line)]] | wt | 22.5 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.172× (z -10.3) |
| [[A-172 (line)]] | wt | 8.42 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.4) |
| [[A-427 (line)]] | wt | 31.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 4.41 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.127× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.105× (z -8.5) |
| [[A549 (line)]] | wt | 6.62 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.03× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 7.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0696× (z -10.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 7.05 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.146× (z -9.0) |
| [[HOP62 (line)]] | alt | 5.40 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 3.85 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0861× (z -8.6) |
| [[LoVo (line)]] | wt | 12.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.227× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 9.89 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0718× (z -13.4) |
| [[A498 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZD4]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[KLHL17]] | +0.68 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[BMP8B]] | +0.66 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[ZDHHC8]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[SHANK3]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[SLC29A4]] | +0.64 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[MMP15]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RTN4R]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |
| [[GNAZ]] | +0.62 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[FOXO6]] | +0.62 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[SSBP4]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SH2B2]] | +0.62 | +0.58 / +0.51 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.55 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[C11orf58]] | -0.54 | -0.40 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF26A]] | B | KIF26A activity raises JAG2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.40× lower at baseline in the lines without KIF26A | 0.002 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[SLC29A4]] | B | SLC29A4 activity raises JAG2's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 2.00× lower at baseline in the lines without SLC29A4 | 0.009 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[BRSK2]] | B | BRSK2 activity raises JAG2's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 2.23× lower at baseline in the lines without BRSK2 | 0.012 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[FBXL16]] | B | FBXL16 activity raises JAG2's level | lines that do not express FBXL16 (7) vs lines expressing it (43) | 2.69× lower at baseline in the lines without FBXL16 | 0.035 | ⚠ within organs, on part of the lines; also absent: SHC2, PLEKHG3 |
| [[ABCA3]] | B | ABCA3 activity raises JAG2's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 2.53× lower at baseline in the lines without ABCA3 | 0.059 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises JAG2's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.88× lower at baseline in the lines without SEPTIN3 | 0.065 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[GJA3]] | B | GJA3 activity raises JAG2's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 1.72× lower at baseline in the lines without GJA3 | 0.065 | ⚠ within organs, on part of the lines; also absent: GBX1 |
| [[GNAZ]] | B | GNAZ activity raises JAG2's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.65× lower at baseline in the lines without GNAZ | 0.078 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers JAG2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers JAG2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 23, C 1. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARD6G]] | B | JAG2 activity raises PARD6G's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without JAG2 | 0.014 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[IMPDH1]] | B | JAG2 activity raises IMPDH1's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without JAG2 | 0.016 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[SLC29A1]] | B | JAG2 activity raises SLC29A1's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.75× lower at baseline in the lines without JAG2 | 0.017 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[EPHB4]] | B | JAG2 activity raises EPHB4's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without JAG2 | 0.029 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[FOXO6]] | B | JAG2 activity raises FOXO6's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.50× lower at baseline in the lines without JAG2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[RTN4R]] | B | JAG2 activity raises RTN4R's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without JAG2 | 0.032 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[SHANK3]] | B | JAG2 activity raises SHANK3's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without JAG2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[RBM38]] | B | JAG2 activity raises RBM38's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without JAG2 | 0.037 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[SEPTIN3]] | B | JAG2 activity raises SEPTIN3's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 2.31× lower at baseline in the lines without JAG2 | 0.041 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[ABCA3]] | B | JAG2 activity raises ABCA3's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 3.15× lower at baseline in the lines without JAG2 | 0.045 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[ARHGAP45]] | B | JAG2 activity raises ARHGAP45's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without JAG2 | 0.045 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[FGFR3]] | B | JAG2 activity raises FGFR3's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.48× lower at baseline in the lines without JAG2 | 0.048 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.8, -1.0); signed map (-23.4, 33.8). **Vector** length 70.0, 13.5% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +3.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -11.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.5 | -7.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | jagged canonical Notch ligand 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:105,140,982-105,168,824 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Canonical Notch ligands |
| Hallmark sets | ANGIOGENESIS, WNT_BETA_CATENIN_SIGNALING, P53_PATHWAY |
| Reactome | 17 pathways, smallest: Constitutive Signaling by NOTCH1 t(7;9)(NOTCH1:M1580_K2555) Translocation Mutant; Signaling by NOTCH1 t(7;9)(NOTCH1:M1580_K2555) Translocation Mutant; Constitutive Signaling by NOTCH1 HD Domain Mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y219](https://www.uniprot.org/uniprotkb/Q9Y219) (Protein jagged-2):

> Putative Notch ligand involved in the mediation of Notch signaling. Involved in limb development (By similarity).

**Summary**, from NCBI Gene [3714](https://www.ncbi.nlm.nih.gov/gene/3714):

> The Notch signaling pathway is an intercellular signaling mechanism that is essential for proper embryonic development. Members of the Notch gene family encode transmembrane receptors that are critical for various cell fate decisions. The protein encoded by this gene is one of several ligands that activate Notch and related receptors. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6189) · Entrez [3714](https://www.ncbi.nlm.nih.gov/gene/3714) · UniProt [Q9Y219](https://www.uniprot.org/uniprotkb/Q9Y219) · Ensembl [ENSG00000184916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184916)

## Data

Gene col 11590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11590); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11590]; `tensor/DDL_lfc|DDL_z.npy` [11590]; `embed/gene_vectors.npy` [11590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11590 or target_col == 11590). Every well: [[JAG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
