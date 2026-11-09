---
symbol: "PHF7"
type: "gene"
col: 207
ensembl_id: "ENSG00000010318"
name: "PHD finger protein 7"
location: "3p21.1"
module: 22
arm: "+"
pooled_cpm: 10.59
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PHF7

*PHD finger protein 7* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.39× (z +9.7, q 1e-19, up in 22 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +7.3, q 5e-11, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.431× (z -10.2, q 1e-21, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR11]] (+0.61, fdr 1e-05), [[RCCD1]] (+0.59, fdr 3e-05), [[CDCA3]] (+0.59, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NEURL1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.39×** | +9.7 | 1e-19 | 22/32 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +7.8 | 2e-12 | 9/17 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.3 | 5e-11 | 23/46 (A498, A549, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +6.7 | 4e-09 | 27/47 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +5.9 | 4e-07 | 25/47 (NCI-H23, KATO III, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +5.4 | 6e-06 | 21/45 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +5.4 | 7e-06 | 26/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.49×** | +4.8 | 9e-05 | 19/47 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +4.8 | 9e-05 | 13/25 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +4.8 | 9e-05 | 14/36 (NCI-H460, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.25×** | +3.8 | 0.008 | 13/48 (A-427, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.34×** | +3.6 | 0.016 | 14/47 (NCI-H23, KATO III, …) | all doses, flat |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.023 | 6/48 (HEC-1-A, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +3.2 | 0.054 | 2/47 (KATO III, NCI-H2347) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.061 | 6/47 (J82, RKO, …) | top dose only | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.061 | 9/47 (A549, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 207.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.431×** | -10.2 | 1e-21 | 37/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.505×** | -7.8 | 2e-12 | 30/46 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.531×** | -7.6 | 4e-12 | 25/45 (A-427, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.567×** | -6.6 | 7e-09 | 24/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.584×** | -6.5 | 1e-08 | 28/47 (PANC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.595×** | -6.3 | 3e-08 | 27/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.611×** | -5.9 | 2e-07 | 24/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.623×** | -5.7 | 8e-07 | 21/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -5.2 | 2e-05 | 20/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.760×** | -4.7 | 2e-04 | 20/44 (PANC-1, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.502×** | -4.3 | 7e-04 | 17/42 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.504×** | -4.3 | 7e-04 | 8/46 (PANC-1, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.692×** | -4.2 | 0.001 | 18/47 (HCT15, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.711×** | -4.1 | 0.002 | 22/45 (PANC-1, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.750×** | -3.5 | 0.021 | 13/47 (COLO 205, AsPC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.608×** | -3.1 | 0.058 | 13/46 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.2 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -15.1) |
| [[A-427 (line)]] | wt | 30.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -15.5) |
| [[A498 (line)]] | wt | 6.11 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0578× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 16.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -11.5) |
| [[SW480 (line)]] | alt | 18.8 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.257× (z -10.2) |
| [[A549 (line)]] | wt | 8.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -12.0) |
| [[COLO 205 (line)]] | alt | 6.42 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0589× (z -8.6) |
| [[HCT15 (line)]] | alt | 9.90 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0441× (z -10.6) |
| [[J82 (line)]] | alt | 10.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0696× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 8.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -8.9) |
| [[LS 180 (line)]] | wt | 6.92 | 0 | 1 | — | [[Ciclopirox (drug)]] 5 µM 0.232× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 5.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0682× (z -9.3) |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -8.7) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR11]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[RCCD1]] | +0.59 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[CDCA3]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[G2E3]] | +0.58 | +0.44 / +0.53 | both halves | 3e-05 | same gene group |
| [[GAS2L3]] | +0.57 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PTTG1]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[DEPDC1B]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[MIS18BP1]] | +0.57 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[PSRC1]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CCNF]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[KIF20A]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[DBF4]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_SPERMATOGENESIS |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | B | NEURL1B activity raises PHF7's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without NEURL1B | 0.087 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[AURKB]] | C | AURKB activity raises PHF7's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.84× lower at baseline in the lines without AURKB | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.3, -56.8); signed map (-49.8, -40.8). **Vector** length 64.4, 10.8% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chk1/Chk2(Cds1) mediated inactivation of Cyclin B:Cdk1 complex* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +2.3 | +5.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.7 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.4 | +6.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.1 | +1.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.8 | -10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.5 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,410,660-52,423,641 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NYD-SP6, HSPC226 |
| Gene groups (HGNC) | PHD finger proteins; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWX1](https://www.uniprot.org/uniprotkb/Q9BWX1) (E3 ubiquitin-protein ligase PHF7):

> E3 ubiquitin-protein ligase which ubiquitinates histone H3 at 'Lys-14' (By similarity). Required for male fertility, via inhibition of SPOP-mediated BRDT degradation when in the presence of acetylated histone H4 in early condensing spermatids (By similarity). Stabilization of BRDT allows it to facilitate histone removal in early condensing spermatids and promote the progression of histone-to-protamine exchange (By similarity). Promotes the expression of steroidogenesis proteins in the testes, …

**Summary**, from NCBI Gene [51533](https://www.ncbi.nlm.nih.gov/gene/51533):

> Spermatogenesis is a complex process regulated by extracellular and intracellular factors as well as cellular interactions among interstitial cells of the testis, Sertoli cells, and germ cells. This gene is expressed in the testis in Sertoli cells but not germ cells. The protein encoded by this gene contains plant homeodomain (PHD) finger domains, also known as leukemia associated protein (LAP) domains, believed to be involved in transcriptional regulation. The protein, which localizes to the …

**Accessions** — [HGNC:18458](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18458) · Entrez [51533](https://www.ncbi.nlm.nih.gov/gene/51533) · UniProt [Q9BWX1](https://www.uniprot.org/uniprotkb/Q9BWX1) · Ensembl [ENSG00000010318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010318)

## Data

Gene col 207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 207); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 207]; `tensor/DDL_lfc|DDL_z.npy` [207]; `embed/gene_vectors.npy` [207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 207 or target_col == 207). Every well: [[PHF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
