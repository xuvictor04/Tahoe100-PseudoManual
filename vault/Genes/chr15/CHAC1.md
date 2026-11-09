---
symbol: "CHAC1"
type: "gene"
col: 4937
ensembl_id: "ENSG00000128965"
name: "ChaC glutathione specific gamma-glutamylcyclotransferase 1"
location: "15q15.1"
module: 63
arm: "+"
pooled_cpm: 5.0
n_lines_expressing: 43
n_dd_up: 30
n_dd_down: 18
n_dd_up_clean: 25
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 11
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# CHAC1

*ChaC glutathione specific gamma-glutamylcyclotransferase 1* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 0.5 µM: 3.15× (z +9.7, q 3e-19, up in 22 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.203× (z -12.9, q 2e-35, down in 32 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASNS]] (+0.88, fdr 7e-06), [[GARS1]] (+0.84, fdr 7e-06), [[MARS1]] (+0.83, fdr 7e-06).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ASNSP1]] → it (grade B ⚠); 11 go from it, the strongest it → [[PYCR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **3.15×** | +9.7 | 3e-19 | 22/29 (NCI-H2030, LoVo, …) | two highest doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **3.05×** | +9.4 | 2e-18 | 29/38 (A498, SW1417, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **2.08×** | +8.7 | 7e-16 | 30/38 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.62×** | +8.1 | 7e-14 | 25/35 (LoVo, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +7.5 | 6e-12 | 21/38 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.72×** | +6.4 | 1e-08 | 18/37 (SW1417, NCI-H460, …) | top dose only | position effect removed |
| [[Neratinib (drug)]] 5 µM |  | **2.02×** | +5.9 | 3e-07 | 14/36 (RKO, C-33 A, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.98×** | +5.8 | 6e-07 | 16/38 (Panc 03.27, C-33 A, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.98×** | +5.7 | 6e-07 | 20/37 (NCI-H2030, HEC-1-A, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.59×** | +5.5 | 2e-06 | 21/39 (LoVo, NCI-H2030, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +5.4 | 4e-06 | 11/38 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.8 | 8e-05 | 4/20 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **3.54×** | +4.7 | 1e-04 | 11/19 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.74×** | +4.7 | 1e-04 | 6/15 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.4 | 5e-04 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.43×** | +4.2 | 8e-04 | 8/37 (COLO 205, NCI-H2030, …) | rises with dose | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.65×** | +4.2 | 8e-04 | 9/37 (HepG2/C3A, NCI-H2030, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +4.0 | 0.002 | 13/37 (SHP-77, C-33 A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.002 | 10/38 (NCI-H2030, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4937.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.203×** | -12.9 | 2e-35 | 32/36 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.388×** | -8.0 | 4e-13 | 25/38 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.442×** | -6.9 | 1e-09 | 22/37 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.583×** | -6.4 | 2e-08 | 18/30 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.480×** | -6.2 | 7e-08 | 16/24 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -5.9 | 3e-07 | 21/39 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.548×** | -5.1 | 3e-05 | 19/35 (A-427, KATO III, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.564×** | -4.8 | 1e-04 | 17/35 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.582×** | -4.6 | 3e-04 | 20/37 (PANC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -4.4 | 5e-04 | 19/37 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.583×** | -4.2 | 0.001 | 14/25 (KATO III, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -4.0 | 0.003 | 16/28 (SW1417, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -3.6 | 0.013 | 17/27 (HT-29, Hs 766T, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -3.5 | 0.021 | 16/28 (SW1417, HT-29, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **0.753×** | -3.4 | 0.026 | 10/37 (H4, C-33 A, …) | rises with dose |  |
| [[Resveratrol (drug)]] 5 µM |  | **0.764×** | -3.2 | 0.047 | 9/37 (C-33 A, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0412× (z -18.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.115× (z -18.0) |
| [[KATO III (line)]] | alt | 13.9 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0561× (z -20.0) |
| [[SW1417 (line)]] | alt | 9.88 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -15.2) |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0290× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0356× (z -17.2) |
| [[LoVo (line)]] | wt | 17.1 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0281× (z -19.6) |
| [[A498 (line)]] | wt | 4.31 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0526× (z -10.9) |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0219× (z -14.4) |
| [[A-427 (line)]] | wt | 4.71 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0681× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -9.4) |
| [[SW48 (line)]] | wt | 8.19 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0332× (z -9.6) |
| [[SW480 (line)]] | alt | 5.57 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -9.5) |
| [[A-172 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASNS]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 807 |
| [[GARS1]] | +0.84 | +0.75 / +0.85 | both halves | 7e-06 |  |
| [[MARS1]] | +0.83 | +0.79 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SESN2]] | +0.83 | +0.76 / +0.84 | both halves | 7e-06 | STRING 608 |
| [[CARS1]] | +0.82 | +0.77 / +0.81 | both halves | 7e-06 | STRING 453 |
| [[GOT1]] | +0.82 | +0.72 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[AARS1]] | +0.81 | +0.76 / +0.84 | both halves | 7e-06 |  |
| [[TRIB3]] | +0.80 | +0.68 / +0.83 | both halves | 7e-06 | pathway: Response of EIF2AK1 (HRI) to heme deficiency; STRING 966 |
| [[SARS1]] | +0.80 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[PHGDH]] | +0.80 | +0.74 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[PSAT1]] | +0.77 | +0.73 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 554 |
| [[ADM2]] | +0.75 | +0.64 / +0.76 | both halves | 7e-06 | STRING 436 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASNSP1]] | B | ASNSP1 activity raises CHAC1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.54× lower at baseline in the lines without ASNSP1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[TOP2A]] | B | TOP2A activity raises CHAC1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC00662]] | C | LINC00662 activity lowers CHAC1's level | lines that do not express LINC00662 (3) vs lines expressing it (47) | 3.28× higher at baseline in the lines without LINC00662 | 0.041 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYCR1]] | B | CHAC1 activity raises PYCR1's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 2.55× lower at baseline in the lines without CHAC1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[ASNS]] | B | CHAC1 activity raises ASNS's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 3.01× lower at baseline in the lines without CHAC1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[CBX4]] | B | CHAC1 activity raises CBX4's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without CHAC1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[SARS1]] | B | CHAC1 activity raises SARS1's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without CHAC1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[NARS1]] | B | CHAC1 activity raises NARS1's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.53× lower at baseline in the lines without CHAC1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[PABPC1L]] | B | CHAC1 activity raises PABPC1L's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without CHAC1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[ADM2]] | B | CHAC1 activity raises ADM2's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.60× lower at baseline in the lines without CHAC1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[AKNA]] | B | CHAC1 activity raises AKNA's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.17× lower at baseline in the lines without CHAC1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[SEPHS2]] | B | CHAC1 activity raises SEPHS2's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without CHAC1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[YARS1]] | B | CHAC1 activity raises YARS1's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without CHAC1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[PCK2]] | B | CHAC1 activity raises PCK2's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without CHAC1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.861). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.3, 48.4); signed map (-13.0, 24.8). **Vector** length 99.1, 25.4% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.65 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.76 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.76 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +5.2 | +8.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.8 | +5.8 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +4.4 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +8.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +9.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.4 | +5.7 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +3.3 | +6.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -12.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -8.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ChaC glutathione specific gamma-glutamylcyclotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,952,962-40,956,512 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4504 |
| Gene groups (HGNC) | Carbon-nitrogen lyases |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 7 pathways, smallest: Glutathione synthesis and recycling; Response of EIF2AK1 (HRI) to heme deficiency; Glutathione conjugation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUX1](https://www.uniprot.org/uniprotkb/Q9BUX1) (Glutathione-specific gamma-glutamylcyclotransferase 1):

> Catalyzes the cleavage of glutathione into 5-oxo-L-proline and a Cys-Gly dipeptide. Acts specifically on glutathione, but not on other gamma-glutamyl peptides. Glutathione depletion is an important factor for apoptosis initiation and execution. Acts as a pro-apoptotic component of the unfolded protein response pathway by mediating the pro-apoptotic effects of the ATF4-ATF3-DDIT3/CHOP cascade. Negative regulator of Notch signaling pathway involved in embryonic neurogenesis: acts by inhibiting …

**Summary**, from NCBI Gene [79094](https://www.ncbi.nlm.nih.gov/gene/79094):

> This gene encodes a member of the gamma-glutamylcyclotransferase family of proteins. The encoded protein has been shown to promote neuronal differentiation by deglycination of the Notch receptor, which prevents receptor maturation and inhibits Notch signaling. This protein may also play a role in the unfolded protein response, and in regulation of glutathione levels and oxidative balance in the cell. Elevated expression of this gene may indicate increased risk of cancer recurrence among breast …

**Accessions** — [HGNC:28680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28680) · Entrez [79094](https://www.ncbi.nlm.nih.gov/gene/79094) · UniProt [Q9BUX1](https://www.uniprot.org/uniprotkb/Q9BUX1) · Ensembl [ENSG00000128965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128965)

## Data

Gene col 4937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4937); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4937]; `tensor/DDL_lfc|DDL_z.npy` [4937]; `embed/gene_vectors.npy` [4937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4937 or target_col == 4937). Every well: [[CHAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
