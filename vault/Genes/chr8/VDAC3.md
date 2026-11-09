---
symbol: "VDAC3"
type: "gene"
col: 1227
ensembl_id: "ENSG00000078668"
name: "voltage dependent anion channel 3"
location: "8p11.21"
module: 65
arm: "+"
pooled_cpm: 49.32
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# VDAC3

*voltage dependent anion channel 3* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.45× (z +5.3, q 8e-05, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.551× (z -11.9, q 4e-30, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACE1]] (+0.78, fdr 7e-06), [[ECI2]] (+0.76, fdr 7e-06), [[PEX3]] (+0.74, fdr 7e-06); moves opposite to [[SKIL]] (-0.70, fdr 1e-05), [[ST7L]] (-0.68, fdr 1e-05), [[KDM6B]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +5.3 | 8e-05 | 30/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.024 | 22/48 (RKO, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.079 | 24/48 (HEC-1-A, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.27×** | +3.4 | 0.096 | 21/47 (PANC-1, A498, …) | two highest doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.096 | 22/48 (SW480, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1227.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.551×** | -11.9 | 4e-30 | 41/48 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.535×** | -8.9 | 2e-16 | 36/48 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.576×** | -7.5 | 1e-11 | 35/48 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -4.6 | 6e-04 | 23/48 (HEC-1-A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.762×** | -3.8 | 0.014 | 24/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.740× | -3.0 | 0.22 | 14/48 (J82, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 73.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 43.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 49.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -13.1) |
| [[A-427 (line)]] | wt | 52.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.6) |
| [[HCT15 (line)]] | alt | 96.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -13.6) |
| [[HS-578T (line)]] | alt | 76.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 48.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 52.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -10.7) |
| [[SNU-1 (line)]] | wt | 71.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0552× (z -20.3) |
| [[AsPC-1 (line)]] | alt | 30.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.3) |
| [[BT-474 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.284× (z -8.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 61.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -9.5) |
| [[H4 (line)]] | wt | 45.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -9.2) |
| [[HOP62 (line)]] | alt | 64.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -8.8) |
| [[Hs 766T (line)]] | wt | 71.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.4) |
| [[J82 (line)]] | alt | 57.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 73.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 42.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 48.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -9.0) |
| [[PANC-1 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 35.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.8) |
| [[A498 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 50.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACE1]] | +0.78 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[ECI2]] | +0.76 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[PEX3]] | +0.74 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[NFRKB]] | +0.73 | +0.71 / +0.60 | both halves | 7e-06 | pathway: Deubiquitination |
| [[ALG9]] | +0.73 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[ATG4C]] | +0.73 | +0.66 / +0.58 | both halves | 8e-06 | pathway: Autophagy |
| [[RELCH]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[UBAC1]] | +0.70 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[MMS19]] | +0.70 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[CRYZL1]] | +0.69 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[USP48]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 | pathway: Deubiquitination |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIL]] | -0.70 | -0.74 / -0.57 | both halves | 1e-05 |  |
| [[ST7L]] | -0.68 | -0.71 / -0.52 | both halves | 1e-05 |  |
| [[KDM6B]] | -0.67 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[FKRP]] | -0.66 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[NANOS3]] | -0.65 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[PCF11]] | -0.65 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[ZNF655]] | -0.64 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[ZC3H4]] | -0.64 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.63 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.63 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.62 | -0.67 / -0.40 | both halves | 4e-05 |  |
| [[THOC6]] | -0.62 | -0.59 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers VDAC3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARAP2]] | B | ARAP2 activity lowers VDAC3's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.42× higher at baseline in the lines without ARAP2 | 0.095 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.817). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (1.9, -9.9); signed map (-34.4, -6.0). **Vector** length 117, 33.8% of its response variance represented; |z| ≥ 3 in 666 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.2 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.9 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.4 | -2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | voltage dependent anion channel 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:42,391,624-42,405,937 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HD-VDAC3 |
| Gene groups (HGNC) | Voltage dependent anion channels |
| Hallmark sets | SPERMATOGENESIS, MYC_TARGETS_V1, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Mitochondrial calcium ion transport; PINK1-PRKN Mediated Mitophagy; Mitophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y277](https://www.uniprot.org/uniprotkb/Q9Y277) (Non-selective voltage-gated ion channel VDAC3):

> Non-selective voltage-gated ion channel that mediates the transport of anions and cations through the mitochondrion outer membrane and plasma membrane. Forms a high-conducting channel with a stable open state and a voltage-induced closure with a mild preference for anions over cations. Involved in male fertility and sperm mitochondrial sheath formation (By similarity).

**Summary**, from NCBI Gene [7419](https://www.ncbi.nlm.nih.gov/gene/7419):

> This gene encodes a voltage-dependent anion channel (VDAC), and belongs to the mitochondrial porin family. VDACs are small, integral membrane proteins that traverse the outer mitochondrial membrane and conduct ATP and other small metabolites. They are known to bind several kinases of intermediary metabolism, thought to be involved in translocation of adenine nucleotides, and are hypothesized to form part of the mitochondrial permeability transition pore, which results in the release of …

**Accessions** — [HGNC:12674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12674) · Entrez [7419](https://www.ncbi.nlm.nih.gov/gene/7419) · UniProt [Q9Y277](https://www.uniprot.org/uniprotkb/Q9Y277) · Ensembl [ENSG00000078668](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078668)

## Data

Gene col 1227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1227); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1227]; `tensor/DDL_lfc|DDL_z.npy` [1227]; `embed/gene_vectors.npy` [1227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1227 or target_col == 1227). Every well: [[VDAC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VDAC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
