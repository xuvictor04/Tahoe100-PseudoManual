---
symbol: "MOB3B"
type: "gene"
col: 4165
ensembl_id: "ENSG00000120162"
name: "MOB kinase activator 3B"
location: "9p21.2"
module: 26
arm: "+"
pooled_cpm: 18.86
n_lines_expressing: 40
n_dd_up: 29
n_dd_down: 10
n_dd_up_clean: 25
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# MOB3B

*MOB kinase activator 3B* — 9p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +11.2, q 4e-26, up in 23 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.349× (z -7.3, q 2e-10, down in 21 of 34 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.557× (z -4.1, q 0.005, down in 13 of 36 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP31]] (+0.53, fdr 2e-04), [[HSD17B3]] (+0.51, fdr 1e-04), [[ST20-MTHFS]] (+0.51, fdr 9e-05); moves opposite to [[FAM161A]] (-0.43, fdr 0.001, ⚠ not reproduced), [[CEP250]] (-0.42, fdr 1e-04), [[PHKA2]] (-0.42, fdr 4e-04), [[FAM13B]] (-0.41, fdr 4e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PLSCR2]] → it (grade B ⚠); 2 go from it, the strongest it → [[C2CD6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +11.2 | 4e-26 | 23/35 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +10.4 | 1e-22 | 26/36 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +8.5 | 3e-15 | 27/38 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +8.1 | 7e-14 | 29/37 (RKO, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +7.7 | 1e-12 | 22/37 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +7.6 | 3e-12 | 22/38 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +6.9 | 3e-10 | 23/38 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +6.6 | 3e-09 | 23/37 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +5.6 | 1e-06 | 20/38 (LS 180, HOP62, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 9e-06 | 20/37 (SK-MEL-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.47×** | +5.1 | 2e-05 | 15/36 (H4, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +5.1 | 2e-05 | 14/38 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **2.05×** | +5.0 | 3e-05 | 18/37 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +4.9 | 5e-05 | 18/38 (SW48, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.001 | 9/37 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.001 | 12/38 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.349×** | -7.3 | 2e-10 | 21/34 (SW 900, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.617×** | -6.4 | 4e-08 | 23/38 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.633×** | -6.1 | 2e-07 | 22/36 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.719×** | -4.4 | 0.002 | 17/38 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **0.733×** | -4.1 | 0.004 | 14/33 (SW 900, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.557×** | -4.1 | 0.005 | 13/36 (Panc 03.27, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.783×** | -3.3 | 0.084 | 17/37 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.632×** | -3.2 | 0.084 | 7/34 (NCI-H1573, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.779×** | -3.2 | 0.084 | 13/37 (J82, SW48, …) | top dose only |  |
| [[Allopurinol (drug)]] 0.05 µM |  | **0.787×** | -3.2 | 0.084 | 7/38 (A549, KATO III, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | 0.647× | -3.0 | 0.13 | 5/33 (A549, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.1 | 1 | 6 (6 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.172× (z -10.9) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 6.04 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.39× (z +9.6) | [[Neratinib (drug)]] 0.05 µM 0.0757× (z -9.4) |
| [[A498 (line)]] | wt | 51.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -13.6) |
| [[J82 (line)]] | alt | 38.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.01× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[LoVo (line)]] | wt | 55.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[SW 900 (line)]] | alt | 29.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0890× (z -8.5) |
| [[H4 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0808× (z -8.8) ⚠ cell-cycle shift, explains ~49% of this change |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0841× (z -10.6) |
| [[LS 180 (line)]] | wt | 75.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[NCI-H2030 (line)]] | alt | 6.13 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0838× (z -9.3) |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0814× (z -8.9) ⚠ toxic |
| [[SW48 (line)]] | wt | 28.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0667× (z -13.4) |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.00 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP31]] | +0.53 | +0.43 / +0.31 | both halves | 2e-04 |  |
| [[HSD17B3]] | +0.51 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[ST20-MTHFS]] | +0.51 | +0.51 / +0.37 | both halves | 9e-05 |  |
| [[MYRFL]] | +0.51 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[SATB1-AS1]] | +0.49 | +0.44 / +0.32 | both halves | 1e-04 |  |
| [[PRKCH-AS1]] | +0.48 | +0.45 / +0.39 | both halves | 6e-05 |  |
| [[LINC02362]] | +0.48 | +0.50 / +0.32 | both halves | 2e-04 |  |
| [[PDC-AS1]] | +0.47 | +0.52 / +0.30 | both halves | 2e-04 |  |
| [[BMAL2-AS1]] | +0.46 | +0.32 / +0.40 | both halves | 2e-04 |  |
| [[CA3]] | +0.46 | +0.46 / +0.31 | both halves | 2e-04 |  |
| [[CAPN3]] | +0.46 | +0.53 / +0.26 | both halves | 3e-04 |  |
| [[LYG1]] | +0.46 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM161A]] | -0.43 | -0.15 / -0.25 | ⚠ not reproduced | 0.001 |  |
| [[CEP250]] | -0.42 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[PHKA2]] | -0.42 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[FAM13B]] | -0.41 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[FN3KRP]] | -0.40 | -0.36 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[ILVBL]] | -0.39 | -0.37 / -0.25 | both halves | 4e-04 |  |
| [[IMMP1L]] | -0.38 | -0.34 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR2]] | B | PLSCR2 activity raises MOB3B's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 2.73× lower at baseline in the lines without PLSCR2 | 0.028 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[GNA14]] | B | GNA14 activity raises MOB3B's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.50× lower at baseline in the lines without GNA14 | 0.028 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[CA3]] | B | CA3 activity raises MOB3B's level | lines that do not express CA3 (10) vs lines expressing it (40) | 2.57× lower at baseline in the lines without CA3 | 0.031 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2 |
| [[ENKUR]] | B | ENKUR activity raises MOB3B's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without ENKUR | 0.039 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MOB3B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SMCO2]] | B | SMCO2 activity raises MOB3B's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.90× lower at baseline in the lines without SMCO2 | 0.086 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2CD6]] | B | MOB3B activity lowers C2CD6's level | lines that do not express MOB3B (10) vs lines expressing it (40) | 1.37× higher at baseline in the lines without MOB3B | 0.047 | ⚠ within organs, on part of the lines; also absent: MYO1D; maybe low, not absent |
| [[CA3]] | B | MOB3B activity raises CA3's level | lines that do not express MOB3B (10) vs lines expressing it (40) | 2.52× lower at baseline in the lines without MOB3B | 0.068 | ⚠ within organs, on part of the lines; also absent: MYO1D; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.361). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (26.8, -11.6); signed map (17.8, 0.8). **Vector** length 60.8, 9.72% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +10.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | -1.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | +5.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.2 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | +7.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | +6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | +1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | MOB kinase activator 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.2 — chr9:27,325,209-27,529,814 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOB1D, FLJ13204; previously MOBKL2B, C9orf35 |
| Gene groups (HGNC) | MOB kinase activators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TA1](https://www.uniprot.org/uniprotkb/Q86TA1) (MOB kinase activator 3B):

> Modulates LATS1 expression in the Hippo signaling pathway which plays a pivotal role in organ size control and tumor suppression by restricting proliferation and promoting apoptosis.

**Summary**, from NCBI Gene [79817](https://www.ncbi.nlm.nih.gov/gene/79817):

> The protein encoded by this gene shares similarity with the yeast Mob1 protein. Yeast Mob1 binds Mps1p, a protein kinase essential for spindle pole body duplication and mitotic checkpoint regulation. This gene is located on the opposite strand as the interferon kappa precursor (IFNK) gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23825) · Entrez [79817](https://www.ncbi.nlm.nih.gov/gene/79817) · UniProt [Q86TA1](https://www.uniprot.org/uniprotkb/Q86TA1) · Ensembl [ENSG00000120162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120162)

## Data

Gene col 4165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4165); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4165]; `tensor/DDL_lfc|DDL_z.npy` [4165]; `embed/gene_vectors.npy` [4165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4165 or target_col == 4165). Every well: [[MOB3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOB3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
