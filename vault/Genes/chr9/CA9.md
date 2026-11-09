---
symbol: "CA9"
type: "gene"
col: 2829
ensembl_id: "ENSG00000107159"
name: "carbonic anhydrase 9"
location: "9p13.3"
module: 103
arm: "+"
pooled_cpm: 18.58
n_lines_expressing: 31
n_dd_up: 0
n_dd_down: 47
n_dd_up_clean: 0
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 7
direction_downstream: 20
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# CA9

*carbonic anhydrase 9* — 9p13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.124× (z -23.7, q 0e+00, down in 27 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRN1]] (+0.59, fdr 2e-05), [[PER2]] (+0.56, fdr 1e-05), [[SMAP2]] (+0.55, fdr 1e-05); moves opposite to [[ULK2]] (-0.57, fdr 1e-05), [[TXNRD3]] (-0.52, fdr 1e-05), [[USP45]] (-0.50, fdr 5e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ADD3-AS1]] → it (grade B ⚠); 20 go from it, the strongest it → [[PER2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.4 | 0.42 | 5/29 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.47× | +3.2 | 0.43 | 9/29 (SNU-423, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2829.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.124×** | -23.7 | 0e+00 | 27/28 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.133×** | -16.2 | 0e+00 | 28/28 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.141×** | -15.8 | 0e+00 | 29/29 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.153×** | -14.6 | 1e-45 | 27/28 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.187×** | -13.5 | 2e-39 | 29/29 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.189×** | -13.4 | 4e-39 | 27/29 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.285×** | -10.1 | 5e-22 | 23/29 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.304×** | -9.2 | 2e-18 | 25/26 (Hs 766T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.382×** | -7.7 | 6e-13 | 25/29 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.397×** | -7.0 | 1e-10 | 26/27 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.406×** | -7.0 | 2e-10 | 21/27 (SW480, H4, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.442×** | -6.5 | 3e-09 | 22/28 (KATO III, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.445×** | -6.5 | 4e-09 | 23/28 (H4, KATO III, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -6.5 | 4e-09 | 23/27 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.461×** | -6.2 | 2e-08 | 20/28 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.488×** | -5.8 | 3e-07 | 26/29 (KATO III, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 94.9 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0325× (z -27.1) |
| [[SW480 (line)]] | alt | 47.2 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0304× (z -36.0) |
| [[HT-29 (line)]] | alt | 69.7 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0367× (z -28.8) |
| [[RPMI-7951 (line)]] | alt | 73.5 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.3) |
| [[HCT15 (line)]] | alt | 67.8 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0183× (z -34.9) |
| [[LS 180 (line)]] | wt | 76.4 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0424× (z -28.2) |
| [[NCI-H460 (line)]] | wt | 20.8 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0640× (z -22.2) |
| [[HOP62 (line)]] | alt | 50.9 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0457× (z -29.0) |
| [[Hs 766T (line)]] | wt | 30.2 | 0 | 8 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0146× (z -21.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0610× (z -20.5) |
| [[KATO III (line)]] | alt | 38.8 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 31.1 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0872× (z -16.3) |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0844× (z -17.1) |
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0718× (z -18.0) |
| [[A549 (line)]] | wt | 15.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0442× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 8.45 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -9.8) |
| [[HS-578T (line)]] | alt | 17.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 9.78 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0906× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 6.85 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0382× (z -11.0) |
| [[SNU-423 (line)]] | alt | 28.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0541× (z -20.7) |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 22.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0822× (z -15.0) |
| [[A-172 (line)]] | wt | 4.75 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0599× (z -9.2) |
| [[J82 (line)]] | alt | 7.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -11.6) |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0546× (z -20.6) |
| [[SW 1088 (line)]] | alt | 98.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -9.3) |
| [[A-427 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.85 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRN1]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[PER2]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SMAP2]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[HOXA13]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[IGFBP2]] | +0.53 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[NDUFA4L2]] | +0.53 | +0.39 / +0.60 | both halves | 5e-05 | STRING 534 |
| [[CXXC5]] | +0.51 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[NXPH4]] | +0.51 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[TBC1D8B]] | +0.50 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[APLN]] | +0.50 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[NDNF]] | +0.48 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[GPI]] | +0.48 | +0.52 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ULK2]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[TXNRD3]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[USP45]] | -0.50 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[CPNE2]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[ZNF37BP]] | -0.48 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[NAE1]] | -0.46 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[TTL]] | -0.46 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[TYRO3]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZNF354A]] | -0.45 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[CROCCP3-1]] | -0.45 | -0.24 / -0.51 | both halves | 5e-04 |  |
| [[TMTC4]] | -0.45 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[N4BP2]] | -0.45 | -0.40 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3-AS1]] | B | ADD3-AS1 activity raises CA9's level | lines that do not express ADD3-AS1 (9) vs lines expressing it (41) | 4.21× lower at baseline in the lines without ADD3-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ADD3, ARHGAP23, ENSG00000286830; maybe low, not absent |
| [[CA12]] | B | CA12 activity raises CA9's level | lines that do not express CA12 (29) vs lines expressing it (21) | 2.20× lower at baseline in the lines without CA12 | 0.039 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[TFF3]] | B | TFF3 activity raises CA9's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.82× lower at baseline in the lines without TFF3 | 0.079 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[FAXC]] | B | FAXC activity lowers CA9's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.65× higher at baseline in the lines without FAXC | 0.094 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[TOP2A]] | B | TOP2A activity raises CA9's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.5% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTPRB]] | B | PTPRB activity raises CA9's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.51× lower at baseline in the lines without PTPRB | 0.0999 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[TNS1]] | C | TNS1 activity raises CA9's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 3.07× lower at baseline in the lines without TNS1 | 0.056 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 19, C 1. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PER2]] | B | CA9 activity raises PER2's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without CA9 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[ZNF395]] | B | CA9 activity raises ZNF395's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without CA9 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[MTCP1]] | B | CA9 activity raises MTCP1's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without CA9 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[SLC2A1]] | B | CA9 activity raises SLC2A1's level | lines that do not express CA9 (19) vs lines expressing it (31) | 2.01× lower at baseline in the lines without CA9 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[ZNF783]] | B | CA9 activity lowers ZNF783's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.35× higher at baseline in the lines without CA9 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[USP45]] | B | CA9 activity lowers USP45's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.42× higher at baseline in the lines without CA9 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[NUP50-DT]] | B | CA9 activity strengthens NUP50-DT's drug response | lines that do not express CA9 (18) vs lines expressing it (29) | the lines without CA9 respond 0.70× as strongly (z diff +1.16); strongest at Idarubicin (hydrochloride) 5 µM: 1.49x vs 2.09x (z diff +2.5) | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970; target measured in part of the lines; artifact flags |
| [[ADD3-AS1]] | B | CA9 activity raises ADD3-AS1's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without CA9 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[TXNRD3]] | B | CA9 activity lowers TXNRD3's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.74× higher at baseline in the lines without CA9 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[RAB20]] | B | CA9 activity raises RAB20's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without CA9 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[ZNF354B]] | B | CA9 activity lowers ZNF354B's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.43× higher at baseline in the lines without CA9 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[BRWD3]] | B | CA9 activity raises BRWD3's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.25× lower at baseline in the lines without CA9 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.5, -13.5); signed map (-32.1, 29.1). **Vector** length 89.1, 26.2% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | -6.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | -2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | -3.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | -0.2 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.6 | -4.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.5 | -4.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.3 | -2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | carbonic anhydrase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,673,928-35,681,159 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MN, CAIX |
| Gene groups (HGNC) | Carbonic anhydrases |
| Reactome | 5 pathways, smallest: Reversible hydration of carbon dioxide; Regulation of gene expression by Hypoxia-inducible Factor; Cellular response to hypoxia |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16790](https://www.uniprot.org/uniprotkb/Q16790) (Carbonic anhydrase 9):

> Catalyzes the interconversion between carbon dioxide and water and the dissociated ions of carbonic acid (i.e. bicarbonate and hydrogen ions).

**Summary**, from NCBI Gene [768](https://www.ncbi.nlm.nih.gov/gene/768):

> Carbonic anhydrases (CAs) are a large family of zinc metalloenzymes that catalyze the reversible hydration of carbon dioxide. They participate in a variety of biological processes, including respiration, calcification, acid-base balance, bone resorption, and the formation of aqueous humor, cerebrospinal fluid, saliva, and gastric acid. They show extensive diversity in tissue distribution and in their subcellular localization. CA IX is a transmembrane protein and is one of only two …

**Accessions** — [HGNC:1383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1383) · Entrez [768](https://www.ncbi.nlm.nih.gov/gene/768) · UniProt [Q16790](https://www.uniprot.org/uniprotkb/Q16790) · Ensembl [ENSG00000107159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107159)

## Data

Gene col 2829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2829); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2829]; `tensor/DDL_lfc|DDL_z.npy` [2829]; `embed/gene_vectors.npy` [2829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2829 or target_col == 2829). Every well: [[CA9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CA9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
