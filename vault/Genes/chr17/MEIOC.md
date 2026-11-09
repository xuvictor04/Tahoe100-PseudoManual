---
symbol: "MEIOC"
type: "gene"
col: 11098
ensembl_id: "ENSG00000180336"
name: "meiosis specific with coiled-coil domain"
location: "17q21.31"
module: 140
arm: "+"
pooled_cpm: 6.05
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# MEIOC

*meiosis specific with coiled-coil domain* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.90× (z +16.5, q 0e+00, up in 30 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.883× (z -4.7, q 0.001, down in 12 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Adenosine (drug)]] 5 µM: 0.775× (z -4.0, q 0.020, down in 10 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[PH-797804 (drug)]] 5 µM in 1 line (A-427 0.0789×); [[Vilanterol (drug)]] 0.05 µM in 1 line (NCI-H661 0.0799×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A6]] (+0.81, fdr 7e-06), [[LRRC4C]] (+0.80, fdr 7e-06), [[USH2A]] (+0.80, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FER1L6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +16.5 | 0e+00 | 30/40 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +11.0 | 2e-25 | 7/8 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +9.8 | 2e-20 | 26/42 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.39×** | +9.5 | 2e-19 | 26/44 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +9.2 | 4e-18 | 16/19 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.7 | 1e-12 | 6/11 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.6 | 2e-06 | 11/22 (NCI-H23, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +5.0 | 4e-05 | 4/19 (NCI-H1573, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +4.9 | 6e-05 | 14/42 (NCI-H1573, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.3 | 0.001 | 7/33 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.003 | 8/41 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.003 | 8/47 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.016 | 6/45 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.026 | 14/40 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +3.3 | 0.037 | 2/44 (SW480, NCI-H1573) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.040 | 12/47 (NCI-H460, NCI-H1573, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.060 | 4/44 (A549, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +3.0 | 0.085 | 2/32 (SW480, A-172) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.095 | 1/33 (NCI-H23) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11098.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[PH-797804 (drug)]] 5 µM in 1 line (A-427 0.0789×); [[Vilanterol (drug)]] 0.05 µM in 1 line (NCI-H661 0.0799×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.883× | -4.7 | 0.001 | 12/48 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Adenosine (drug)]] 5 µM |  | **0.775×** | -4.0 | 0.020 | 10/47 (SNU-1, COLO 205, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | **0.713×** | -3.7 | 0.037 | 9/46 (Hs 766T, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 77.0 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0789× (z -8.6) |
| [[A549 (line)]] | wt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 2.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.11× (z +11.2) | — |
| [[LoVo (line)]] | wt | 2.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 2.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +13.9) | — |
| [[NCI-H661 (line)]] | alt | 42.9 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0799× (z -8.5) |
| [[A-172 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A6]] | +0.81 | +0.68 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[LRRC4C]] | +0.80 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[USH2A]] | +0.80 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.80 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.78 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.77 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[ASB14]] | +0.77 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[LINC02006]] | +0.77 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.77 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.76 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[MYO16]] | +0.76 | +0.72 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FER1L6]] | B | FER1L6 activity lowers MEIOC's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.99× higher at baseline in the lines without FER1L6 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[LY96]] | B | LY96 activity lowers MEIOC's level | lines that do not express LY96 (18) vs lines expressing it (32) | 1.25× higher at baseline in the lines without LY96 | 0.081 | ⚠ within organs, on part of the lines; also absent: SOX5, ENSG00000287100, ENSG00000287622; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.1, 28.8); signed map (32.6, 13.4). **Vector** length 41.6, 4.24% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +16.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -1.6 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | meiosis specific with coiled-coil domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,656,404-44,690,308 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35848; previously C17orf104 |
| Matched by | ensembl_id |

**Function**, from UniProt [A2RUB1](https://www.uniprot.org/uniprotkb/A2RUB1) (Meiosis-specific coiled-coil domain-containing protein MEIOC):

> Is required for meiosis completion in both male and female germ cells. Confers stability to numerous meiotic mRNAs in gonads allowing proper initiation and progression into meiosis prophase I. The function may involve YTHDC2 and is independent of induction by retinoic acid (RA). Maintains an extended meiotic prophase I by properly promoting the transition from a mitotic to a meiotic cell cycle program by binding transcripts through its interaction with YTHDC2 that regulate the mitotic cell …

**Summary**, from NCBI Gene [284071](https://www.ncbi.nlm.nih.gov/gene/284071):

> Predicted to be involved in several processes, including germ cell development; germline cell cycle switching, mitotic to meiotic cell cycle; and meiosis I. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26670) · Entrez [284071](https://www.ncbi.nlm.nih.gov/gene/284071) · UniProt [A2RUB1](https://www.uniprot.org/uniprotkb/A2RUB1) · Ensembl [ENSG00000180336](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180336)

## Data

Gene col 11098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11098); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11098]; `tensor/DDL_lfc|DDL_z.npy` [11098]; `embed/gene_vectors.npy` [11098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11098 or target_col == 11098). Every well: [[MEIOC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEIOC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
