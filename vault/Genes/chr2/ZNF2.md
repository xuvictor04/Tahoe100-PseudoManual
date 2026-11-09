---
symbol: "ZNF2"
type: "gene"
col: 15840
ensembl_id: "ENSG00000275111"
name: "zinc finger protein 2"
location: "2q11.1"
module: 107
arm: "+"
pooled_cpm: 5.58
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# ZNF2

*zinc finger protein 2* — 2q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.92× (z +10.8, q 2e-24, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.508× (z -11.3, q 8e-27, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZKSCAN4]] (+0.66, fdr 1e-05), [[ALKBH3]] (+0.65, fdr 7e-06), [[FASTKD3]] (+0.65, fdr 1e-05); moves opposite to [[PEAK1]] (-0.60, fdr 2e-05), [[MAGI3]] (-0.59, fdr 2e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF613]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15840.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +10.8 | 2e-24 | 32/47 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +7.6 | 7e-12 | 15/33 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +7.5 | 1e-11 | 17/47 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +6.2 | 1e-07 | 16/47 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.5 | 3e-06 | 13/46 (LS 180, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +5.1 | 2e-05 | 3/15 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.23×** | +4.9 | 1e-04 | 8/46 (CFPAC-1, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 4e-04 | 9/46 (KATO III, A498, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.006 | 3/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.18× | +3.8 | 0.008 | 13/41 (PANC-1, SW480, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.019 | 4/47 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.22×** | +3.3 | 0.046 | 3/47 (A498, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.046 | 3/47 (BT-474, CHP-212, …) | all doses, flat |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.1 | 0.077 | 2/47 (PANC-1, A-172) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.21×** | +3.1 | 0.077 | 3/33 (NCI-H2347, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.082 | 7/40 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.508×** | -11.3 | 8e-27 | 28/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.601×** | -8.5 | 6e-15 | 22/40 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.699×** | -6.0 | 4e-07 | 14/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.712×** | -5.7 | 2e-06 | 10/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.726×** | -5.1 | 3e-05 | 12/36 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.737×** | -5.1 | 3e-05 | 13/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.757×** | -4.7 | 3e-04 | 8/46 (H4, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **0.781×** | -4.1 | 0.003 | 19/27 (A549, SW1417, …) | inconsistent across doses | composition shift |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | **0.771×** | -4.0 | 0.004 | 3/46 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.05 µM |  | **0.789×** | -3.7 | 0.014 | 12/46 (SW480, AN3 CA, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.824×** | -3.3 | 0.059 | 3/47 (C-33 A, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Malotilate (drug)]] 0.5 µM |  | **0.831×** | -3.1 | 0.086 | 7/44 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.831×** | -3.1 | 0.086 | 8/45 (hTERT-HPNE, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.828×** | -3.0 | 0.097 | 8/45 (NCI-H1573, NCI-H460, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.60 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 3.14 | 0 | 2 (2 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0788× (z -10.3) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 6.26 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -10.4) |
| [[A-172 (line)]] | wt | 5.32 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0820× (z -10.2) |
| [[A549 (line)]] | wt | 7.67 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[C32 (line)]] | wt | 6.95 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 4.71 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 4.31 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0568× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 6.67 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0656× (z -11.2) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 6.49 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0740× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0460× (z -19.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 6.32 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0854× (z -9.6) |
| [[SHP-77 (line)]] | alt | 8.44 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.123× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 8.00 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0906× (z -10.5) |
| [[SNU-1 (line)]] | wt | 7.94 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0775× (z -8.8) |
| [[SW1417 (line)]] | alt | 5.39 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[A-427 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN4]] | +0.66 | +0.74 / +0.55 | both halves | 1e-05 | same gene group |
| [[ALKBH3]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[FASTKD3]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[MIEF1]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MTERF4]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[RBAK]] | +0.63 | +0.67 / +0.48 | both halves | 2e-05 | same gene group |
| [[CBLL1]] | +0.63 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[ZNF777]] | +0.63 | +0.69 / +0.53 | both halves | 1e-05 | same gene group |
| [[ZNF329]] | +0.62 | +0.57 / +0.60 | both halves | 8e-06 | same gene group |
| [[ZSCAN20]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 | same gene group |
| [[RBSN]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 | same gene group |
| [[ALKBH4]] | +0.61 | +0.64 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAK1]] | -0.60 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[MAGI3]] | -0.59 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF613]] | B | ZNF613 activity raises ZNF2's level | lines that do not express ZNF613 (7) vs lines expressing it (43) | 1.42× lower at baseline in the lines without ZNF613 | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF850, ENSG00000283201, ZNF571 |
| [[BOLA3-DT]] | B | BOLA3-DT activity raises ZNF2's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 1.48× lower at baseline in the lines without BOLA3-DT | 0.016 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[ZNF567]] | B | ZNF567 activity raises ZNF2's level | lines that do not express ZNF567 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without ZNF567 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, ZFP14; its own permutation p |
| [[ZNF569]] | B | ZNF569 activity raises ZNF2's level | lines that do not express ZNF569 (14) vs lines expressing it (36) | 1.27× lower at baseline in the lines without ZNF569 | 0.071 | ⚠ within organs, on part of the lines; also absent: ZNF570, PEG10, DNAAF9 |
| [[ZNF223]] | B | ZNF223 activity raises ZNF2's level | lines that do not express ZNF223 (11) vs lines expressing it (39) | 1.16× lower at baseline in the lines without ZNF223 | 0.072 | ⚠ within organs, on part of the lines; also absent: ZNF284, TGFB1I1, ZNF891 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.5, 6.5); signed map (-10.6, -16.8). **Vector** length 39.6, 3.50% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +7.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.9 | -0.2 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -0.6 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.6 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.6 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.05 µM |  | -0.6 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.1 — chr2:95,165,432-95,184,317 (+) |
| Ensembl biotype | protein_coding |
| Also known as | A1-5, ZNF661, Zfp661 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSG1](https://www.uniprot.org/uniprotkb/Q9BSG1) (Zinc finger protein 2):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7549](https://www.ncbi.nlm.nih.gov/gene/7549):

> The protein encoded by this gene belongs to the C2H2-type zinc-finger protein family. The exact function of this gene is not known, however, zinc-finger proteins are known to interact with DNA and function as transcription regulators. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:12991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12991) · Entrez [7549](https://www.ncbi.nlm.nih.gov/gene/7549) · UniProt [Q9BSG1](https://www.uniprot.org/uniprotkb/Q9BSG1) · Ensembl [ENSG00000275111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275111)

## Data

Gene col 15840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15840); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15840]; `tensor/DDL_lfc|DDL_z.npy` [15840]; `embed/gene_vectors.npy` [15840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15840 or target_col == 15840). Every well: [[ZNF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
