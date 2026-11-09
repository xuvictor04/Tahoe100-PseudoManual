---
symbol: "MOB3C"
type: "gene"
col: 6669
ensembl_id: "ENSG00000142961"
name: "MOB kinase activator 3C"
location: "1p33"
module: 80
arm: "+"
pooled_cpm: 4.88
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# MOB3C

*MOB kinase activator 3C* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.72× (z +8.2, q 2e-13, up in 19 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.406× (z -9.6, q 7e-19, down in 29 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.671× (z -4.2, q 0.002, down in 15 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NANOS3]] (+0.62, fdr 1e-05), [[HDX]] (+0.59, fdr 2e-05), [[BRPF3]] (+0.59, fdr 1e-05); moves opposite to [[IARS2]] (-0.58, fdr 1e-05), [[NDC1]] (-0.57, fdr 1e-05), [[ATRN]] (-0.55, fdr 3e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TLR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +8.2 | 2e-13 | 19/37 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.041 | 5/34 (SNU-423, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.7 | 0.041 | 5/34 (COLO 205, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | 1.36× | +3.3 | 0.11 | 2/46 (H4, A498) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.81× | +3.3 | 0.11 | 2/15 (CFPAC-1, AsPC-1) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6669.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.406×** | -9.6 | 7e-19 | 29/46 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.452×** | -8.4 | 1e-14 | 34/46 (AsPC-1, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.501×** | -7.3 | 4e-11 | 28/44 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.576×** | -5.9 | 7e-07 | 23/46 (LS 180, SW1417, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.604×** | -5.3 | 1e-05 | 19/36 (LoVo, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.629×** | -4.9 | 9e-05 | 15/43 (LoVo, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.671×** | -4.2 | 0.002 | 15/46 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.467×** | -4.2 | 0.002 | 17/40 (AsPC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.759×** | -4.1 | 0.002 | 23/36 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.640×** | -3.6 | 0.018 | 10/34 (PANC-1, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.539×** | -3.4 | 0.030 | 8/37 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.654×** | -3.4 | 0.030 | 11/36 (H4, SW480, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.709×** | -3.1 | 0.090 | 9/46 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.749×** | -3.1 | 0.090 | 7/45 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.752×** | -3.0 | 0.098 | 11/44 (SW48, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 7.36 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0230× (z -18.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 8.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.0) | — |
| [[A498 (line)]] | wt | 7.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 5.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 5.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0695× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.19 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0675× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 7.42 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0650× (z -8.6) |
| [[PANC-1 (line)]] | alt | 2.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +9.8) | — |
| [[A-427 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NANOS3]] | +0.62 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[HDX]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[BRPF3]] | +0.59 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[STX4]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ELF4]] | +0.58 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[MC1R]] | +0.58 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[SYNPO]] | +0.57 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[CFAP46]] | +0.57 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ETV7]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ZNF641]] | +0.57 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[AKT1S1]] | +0.56 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[CD2BP2]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IARS2]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[NDC1]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ATRN]] | -0.55 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[BCKDHB]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[KIAA1958]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PRDX4]] | -0.53 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[HDAC3]] | -0.53 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[FOXJ3]] | -0.53 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[PEBP1]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SUMF2]] | -0.53 | -0.54 / -0.43 | both halves | 4e-05 |  |
| [[NME2]] | -0.53 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[HDHD5]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR1]] | B | TLR1 activity raises MOB3C's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 1.43× lower at baseline in the lines without TLR1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[TLR6]] | B | TLR6 activity raises MOB3C's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without TLR6 | 0.008 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[HLA-F]] | B | HLA-F activity raises MOB3C's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.68× lower at baseline in the lines without HLA-F | 0.008 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[CBFA2T3]] | B | CBFA2T3 activity lowers MOB3C's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.37× higher at baseline in the lines without CBFA2T3 | 0.009 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[GBP5]] | B | GBP5 activity raises MOB3C's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 1.38× lower at baseline in the lines without GBP5 | 0.024 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[LACC1]] | B | LACC1 activity raises MOB3C's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.61× lower at baseline in the lines without LACC1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[HLA-K]] | B | HLA-K activity raises MOB3C's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.32× lower at baseline in the lines without HLA-K | 0.057 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[ZC3H12A]] | B | ZC3H12A activity raises MOB3C's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.93× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[CACNG8]] | B | CACNG8 activity strengthens MOB3C's drug response | lines that do not express CACNG8 (14) vs lines expressing it (33) | the lines without CACNG8 respond 0.64× as strongly (z diff +0.67); strongest at Panobinostat 0.05 µM: 0.87x vs 0.57x (z diff +1.4) | 0.076 | ⚠ within organs, on part of the lines; also absent: CACNG6, GAB3, KHDC1; target measured in part of the lines; artifact flags |
| [[HERC6]] | B | HERC6 activity raises MOB3C's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without HERC6 | 0.090 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[TRIP6]] | B | TRIP6 activity raises MOB3C's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.61× lower at baseline in the lines without TRIP6 | 0.098 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, 7.2); signed map (28.6, 9.7). **Vector** length 62.2, 9.57% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.8 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.1 | +1.3 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +1.6 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.0 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +0.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.1 | -8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.0 | -7.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.8 | -9.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | MOB kinase activator 3C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:46,607,719-46,616,811 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOB1E; previously MOBKL2C |
| Gene groups (HGNC) | MOB kinase activators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70IA8](https://www.uniprot.org/uniprotkb/Q70IA8) (MOB kinase activator 3C):

> May regulate the activity of kinases.

**Summary**, from NCBI Gene [148932](https://www.ncbi.nlm.nih.gov/gene/148932):

> The protein encoded by this gene is similar to the yeast Mob1 protein. Yeast Mob1 binds Mps1p, a protein kinase essential for spindle pole body duplication and mitotic checkpoint regulation. Alternatively spliced transcript variants encoding distinct isoforms have been observed. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:29800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29800) · Entrez [148932](https://www.ncbi.nlm.nih.gov/gene/148932) · UniProt [Q70IA8](https://www.uniprot.org/uniprotkb/Q70IA8) · Ensembl [ENSG00000142961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142961)

## Data

Gene col 6669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6669); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6669]; `tensor/DDL_lfc|DDL_z.npy` [6669]; `embed/gene_vectors.npy` [6669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6669 or target_col == 6669). Every well: [[MOB3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOB3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
