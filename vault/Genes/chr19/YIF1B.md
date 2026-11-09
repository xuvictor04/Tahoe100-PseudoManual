---
symbol: "YIF1B"
type: "gene"
col: 9510
ensembl_id: "ENSG00000167645"
name: "Yip1 interacting factor homolog B, membrane trafficking protein"
location: "19q13.2"
module: 85
arm: "+"
pooled_cpm: 13.2
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# YIF1B

*Yip1 interacting factor homolog B, membrane trafficking protein* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.40× (z +8.5, q 8e-15, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.580× (z -7.5, q 4e-11, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCMT1]] (+0.79, fdr 4e-05), [[ANAPC11]] (+0.77, fdr 7e-06), [[PEDS1]] (+0.77, fdr 1e-05); moves opposite to [[MMADHC-DT]] (-0.75, fdr 9e-04, ⚠ one half only (not replicated)), [[PBLD]] (-0.74, fdr 0.002, ⚠ one half only (not replicated)), [[RBMX]] (-0.72, fdr 3e-05), [[IQCH-AS1]] (-0.72, fdr 4e-04), [[ST7L]] (-0.72, fdr 2e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GRIP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.40×** | +8.5 | 8e-15 | 39/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.19×** | +7.7 | 5e-12 | 38/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.07×** | +7.1 | 3e-10 | 34/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.93×** | +5.7 | 1e-06 | 20/35 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.71×** | +5.3 | 2e-05 | 28/45 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.69×** | +4.9 | 1e-04 | 18/26 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.45×** | +3.3 | 0.059 | 13/31 (A549, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.40×** | +3.3 | 0.059 | 16/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.3 | 0.059 | 17/41 (C-33 A, SHP-77, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.098 | 15/44 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9510.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.580×** | -7.5 | 4e-11 | 34/47 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.584×** | -5.2 | 5e-05 | 26/45 (H4, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.637×** | -4.1 | 0.007 | 19/46 (RPMI-7951, RKO, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.765×** | -3.7 | 0.034 | 17/48 (HS-578T, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 7.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0886× (z -9.4) |
| [[H4 (line)]] | wt | 39.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0393× (z -17.0) |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0802× (z -9.5) |
| [[HT-29 (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.5) |
| [[J82 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.9) |
| [[KATO III (line)]] | alt | 12.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.03× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -9.8) |
| [[SW48 (line)]] | wt | 14.3 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0815× (z -9.7) |
| [[SW480 (line)]] | alt | 9.47 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.09× (z +8.5) | — |
| [[A-172 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | +0.79 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[ANAPC11]] | +0.77 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PEDS1]] | +0.77 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[RRAS]] | +0.77 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[MPG]] | +0.74 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[METTL26]] | +0.74 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[SLC27A1]] | +0.74 | +0.63 / +0.33 | both halves | 1e-04 |  |
| [[ARL3]] | +0.74 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[SNAPC3]] | +0.73 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.73 | +0.61 / +0.32 | both halves | 1e-04 |  |
| [[PIGH]] | +0.72 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[TMEM256]] | +0.72 | +0.64 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | -0.75 | -0.69 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[PBLD]] | -0.74 | -0.63 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[RBMX]] | -0.72 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[IQCH-AS1]] | -0.72 | -0.69 / -0.24 | both halves | 4e-04 |  |
| [[ST7L]] | -0.72 | -0.68 / -0.30 | both halves | 2e-04 |  |
| [[EFCAB2]] | -0.72 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[PCBP1-AS1]] | -0.72 | -0.62 / -0.18 | ⚠ one half (not replicated) | 0.001 |  |
| [[CCDC90B-AS1]] | -0.71 | -0.65 / -0.05 | ⚠ one half (not replicated) | 0.005 |  |
| [[GALNT7-DT]] | -0.70 | -0.59 / -0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[WARS2-AS1]] | -0.70 | -0.65 / -0.20 | both halves | 7e-04 |  |
| [[PRRC2B]] | -0.70 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[GABPB2]] | -0.70 | -0.66 / -0.27 | both halves | 3e-04 |  |
| [[KRR1]] | -0.69 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CRPPA]] | -0.68 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[TAFA2]] | -0.68 | -0.63 / -0.22 | both halves | 6e-04 |  |
| [[PSMD6-AS1]] | -0.68 | -0.55 / -0.43 | both halves | 4e-05 |  |
| [[ZMYND11]] | -0.68 | -0.48 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIP1]] | B | GRIP1 activity lowers YIF1B's level | lines that do not express GRIP1 (13) vs lines expressing it (37) | 1.35× higher at baseline in the lines without GRIP1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PAX9; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers YIF1B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.863). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.7, -1.6); signed map (-32.1, 15.7). **Vector** length 75.7, 17.3% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.2 | +8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.8 | +7.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.3 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.1 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.3 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | Yip1 interacting factor homolog B, membrane trafficking protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,303,558-38,317,273 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FinGER8 |
| Gene groups (HGNC) | YIP superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5BJH7](https://www.uniprot.org/uniprotkb/Q5BJH7) (Protein YIF1B):

> Functions in endoplasmic reticulum to Golgi vesicle-mediated transport and regulates the proper organization of the endoplasmic reticulum and the Golgi (By similarity). Plays a key role in targeting to neuronal dendrites receptors such as HTR1A (By similarity). Plays also a role in primary cilium and sperm flagellum assembly probably through protein transport to these compartments.

**Summary**, from NCBI Gene [90522](https://www.ncbi.nlm.nih.gov/gene/90522):

> Involved in endoplasmic reticulum to Golgi vesicle-mediated transport. Located in Golgi apparatus; endoplasmic reticulum; and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30511](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30511) · Entrez [90522](https://www.ncbi.nlm.nih.gov/gene/90522) · UniProt [Q5BJH7](https://www.uniprot.org/uniprotkb/Q5BJH7) · Ensembl [ENSG00000167645](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167645)

## Data

Gene col 9510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9510); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9510]; `tensor/DDL_lfc|DDL_z.npy` [9510]; `embed/gene_vectors.npy` [9510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9510 or target_col == 9510). Every well: [[YIF1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YIF1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
