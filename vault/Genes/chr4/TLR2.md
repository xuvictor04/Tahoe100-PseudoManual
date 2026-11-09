---
symbol: "TLR2"
type: "gene"
col: 6016
ensembl_id: "ENSG00000137462"
name: "toll like receptor 2"
location: "4q31.3"
module: 98
arm: "+"
pooled_cpm: 7.6
n_lines_expressing: 24
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 24
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 15
direction_downstream: 28
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# TLR2

*toll like receptor 2* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 2.61× (z +9.1, q 6e-17, up in 15 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.567× (z -5.4, q 5e-05, down in 13 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRAK3]] (+0.82, fdr 7e-06), [[MT1M]] (+0.73, fdr 7e-06), [[KLF9]] (+0.70, fdr 7e-06); moves opposite to [[AMIGO2]] (-0.51, fdr 2e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 28 go from it, the strongest it → [[B4GALT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.61×** | +9.1 | 6e-17 | 15/20 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.28×** | +7.8 | 1e-12 | 14/20 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +7.8 | 1e-12 | 13/21 (CFPAC-1, A549, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.26×** | +7.7 | 1e-12 | 16/21 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.06×** | +6.9 | 7e-10 | 15/21 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.65×** | +6.7 | 1e-09 | 16/21 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.12×** | +6.6 | 3e-09 | 12/20 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.04×** | +6.5 | 5e-09 | 13/21 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +6.5 | 6e-09 | 12/21 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.92×** | +6.2 | 3e-08 | 13/20 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.91×** | +6.1 | 5e-08 | 15/21 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **1.87×** | +6.0 | 1e-07 | 13/21 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.82×** | +5.7 | 5e-07 | 8/18 (NCI-H1573, NCI-H1792, …) | two highest doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.6 | 9e-07 | 16/21 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **1.78×** | +5.5 | 1e-06 | 16/21 (CFPAC-1, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6016.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.567×** | -5.4 | 5e-05 | 13/21 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.640×** | -4.2 | 0.007 | 10/21 (NCI-H1792, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -3.7 | 0.039 | 15/21 (Panc 03.27, RPMI-7951, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.702× | -3.3 | 0.12 | 9/21 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.718× | -3.1 | 0.18 | 7/21 (SK-MEL-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | 0.533× | -3.1 | 0.18 | 5/19 (HS-578T, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.725× | -3.0 | 0.18 | 3/20 (LoVo, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.708× | -3.0 | 0.18 | 0/21 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 21.0 | 13 | 2 (2 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 7.00× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 130 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0446× (z -30.6) |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0679× (z -20.6) |
| [[SK-MEL-2 (line)]] | alt | 39.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -18.1) |
| [[Panc 03.27 (line)]] | alt | 29.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0934× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.220× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0748× (z -14.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 3.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0523× (z -9.0) ⚠ cell-cycle shift, explains ~17% of this change |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0391× (z -9.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 7.12 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 7.38× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 3.44 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 12.6× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.104× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.733 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.559 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.83 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRAK3]] | +0.82 | +0.74 / +0.83 | both halves | 7e-06 | pathway: MyD88:MAL(TIRAP) cascade initiated on plasma membrane; STRING 852 |
| [[MT1M]] | +0.73 | +0.67 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[KLF9]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[VSTM2L]] | +0.70 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[FKBP5]] | +0.70 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SAA1]] | +0.69 | +0.56 / +0.69 | both halves | 1e-05 | pathway: MyD88:MAL(TIRAP) cascade initiated on plasma membrane; STRING 630 |
| [[MAOA]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CCND3]] | +0.67 | +0.65 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[SAA2]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 | STRING 615 |
| [[RNF175]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 | ⚠ same locus (3.9 kb: neighbours can correlate without regulation) |
| [[MT1X]] | +0.66 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[MT1F]] | +0.65 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[ZMYND8]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMIGO2]] | -0.51 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 7, C 8. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises TLR2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[A4GALT]] | B | A4GALT activity raises TLR2's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 2.36× lower at baseline in the lines without A4GALT | 0.061 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[SH3TC1]] | B | SH3TC1 activity raises TLR2's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.87× lower at baseline in the lines without SH3TC1 | 0.079 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[RIPOR2]] | B | RIPOR2 activity raises TLR2's level | lines that do not express RIPOR2 (9) vs lines expressing it (41) | 2.38× lower at baseline in the lines without RIPOR2 | 0.082 | ⚠ within organs, on part of the lines; also absent: GNA14, EPHA1-AS1; maybe low, not absent |
| [[IRX3]] | B | IRX3 activity raises TLR2's level | lines that do not express IRX3 (9) vs lines expressing it (41) | 2.88× lower at baseline in the lines without IRX3 | 0.088 | ⚠ within organs, on part of the lines; also absent: DYSF, DRAM1, LINC02609 |
| [[GLUL]] | B | GLUL activity raises TLR2's level | lines that do not express GLUL (10) vs lines expressing it (40) | 2.50× lower at baseline in the lines without GLUL | 0.091 | ⚠ within organs, on part of the lines |
| [[GLRX]] | B | GLRX activity raises TLR2's level | lines that do not express GLRX (10) vs lines expressing it (40) | 2.40× lower at baseline in the lines without GLRX | 0.094 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[SAA1]] | C | SAA1 activity raises TLR2's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 2.31× lower at baseline in the lines without SAA1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11; co-absent with the target |
| [[HSD11B1]] | C | HSD11B1 activity raises TLR2's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without HSD11B1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA; co-absent with the target |
| [[LOX]] | C | LOX activity raises TLR2's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.53× lower at baseline in the lines without LOX | 0.048 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[LPAR1]] | C | LPAR1 activity raises TLR2's level | lines that do not express LPAR1 (15) vs lines expressing it (35) | 2.60× lower at baseline in the lines without LPAR1 | 0.066 | ⚠ within organs, on part of the lines; also absent: SVEP1, PAPSS2, TOX2; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises TLR2's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.48× lower at baseline in the lines without GYPC | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 22, C 6. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALT1]] | B | TLR2 activity raises B4GALT1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.80× lower at baseline in the lines without TLR2 | 0.006 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[ADPRHL1]] | B | TLR2 activity raises ADPRHL1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.52× lower at baseline in the lines without TLR2 | 0.010 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[A4GALT]] | B | TLR2 activity raises A4GALT's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without TLR2 | 0.011 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[GLUL]] | B | TLR2 activity raises GLUL's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 2.23× lower at baseline in the lines without TLR2 | 0.019 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[UBE2E1]] | B | TLR2 activity raises UBE2E1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.42× lower at baseline in the lines without TLR2 | 0.022 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[SH3TC1]] | B | TLR2 activity raises SH3TC1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.82× lower at baseline in the lines without TLR2 | 0.045 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[TSC22D3]] | B | TLR2 activity raises TSC22D3's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without TLR2 | 0.047 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[ESYT2]] | B | TLR2 activity strengthens ESYT2's drug response | lines that do not express TLR2 (26) vs lines expressing it (23) | the lines without TLR2 respond 0.70× as strongly (z diff +2.19); strongest at Homoharringtonine 0.5 µM: 0.70x vs 0.44x (z diff +3.3) | 0.049 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA; target measured in part of the lines; artifact flags |
| [[SAMSN1]] | B | TLR2 activity raises SAMSN1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without TLR2 | 0.056 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[SUSD6]] | B | TLR2 activity raises SUSD6's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without TLR2 | 0.068 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[PIK3R1]] | B | TLR2 activity raises PIK3R1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.25× lower at baseline in the lines without TLR2 | 0.075 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[KCNB1]] | B | TLR2 activity lowers KCNB1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.21× higher at baseline in the lines without TLR2 | 0.079 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.778). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.2, 15.1); signed map (16.7, 30.9). **Vector** length 83.4, 25.4% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.4 | +7.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.2 | +6.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.1 | +9.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.0 | +6.2 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -5.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -2.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | toll like receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:153,684,050-153,706,260 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIL4, CD282 |
| Gene groups (HGNC) | CD molecules; Toll like receptors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 29 pathways, smallest: Defensins; Modulation by Mtb of host immune system; Antimicrobial peptides |
| Matched by | ensembl_id |

**Function**, from UniProt [O60603](https://www.uniprot.org/uniprotkb/O60603) (Toll-like receptor 2):

> Cooperates with LY96 to mediate the innate immune response to bacterial lipoproteins and other microbial cell wall components. Cooperates with TLR1 or TLR6 to mediate the innate immune response to bacterial lipoproteins or lipopeptides. Acts via MYD88 and TRAF6, leading to NF-kappa-B activation, cytokine secretion and the inflammatory response. May also activate immune cells and promote apoptosis in response to the lipid moiety of lipoproteins. Recognizes mycoplasmal macrophage-activating …

**Summary**, from NCBI Gene [7097](https://www.ncbi.nlm.nih.gov/gene/7097):

> The protein encoded by this gene is a member of the Toll-like receptor (TLR) family which plays a fundamental role in pathogen recognition and activation of innate immunity. TLRs are highly conserved from Drosophila to humans and share structural and functional similarities. This protein is a cell-surface protein that can form heterodimers with other TLR family members to recognize conserved molecules derived from microorganisms known as pathogen-associated molecular patterns (PAMPs). …

**Accessions** — [HGNC:11848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11848) · Entrez [7097](https://www.ncbi.nlm.nih.gov/gene/7097) · UniProt [O60603](https://www.uniprot.org/uniprotkb/O60603) · Ensembl [ENSG00000137462](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137462)

## Data

Gene col 6016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6016); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6016]; `tensor/DDL_lfc|DDL_z.npy` [6016]; `embed/gene_vectors.npy` [6016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6016 or target_col == 6016). Every well: [[TLR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
