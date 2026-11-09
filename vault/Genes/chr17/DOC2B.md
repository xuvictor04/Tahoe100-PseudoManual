---
symbol: "DOC2B"
type: "gene"
col: 15732
ensembl_id: "ENSG00000272636"
name: "double C2 domain beta"
location: "17p13.3"
module: 9
arm: "+"
pooled_cpm: 3.24
n_lines_expressing: 24
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# DOC2B

*double C2 domain beta* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.33× (z +11.1, q 7e-26, up in 7 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Mebendazole (drug)]] 5 µM: 0.617× (z -4.4, q 0.007, down in 7 of 21 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0846×, RKO 0.104×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.222×); [[Decitabine (drug)]] 0.05 µM in 1 line (RKO 0.0889×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCND3]] (+0.64, fdr 7e-06), [[SLCO3A1]] (+0.55, fdr 1e-05), [[DOK5]] (+0.54, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KCND3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.33×** | +11.1 | 7e-26 | 7/15 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +10.3 | 3e-22 | 1/3 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +8.2 | 4e-14 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +7.6 | 5e-12 | 7/21 (HT-29, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +7.3 | 3e-11 | 4/16 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.2 | 5e-08 | 1/11 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.28×** | +5.5 | 4e-06 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +4.9 | 6e-05 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.9 | 0.006 | 0/15 | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +3.7 | 0.010 | 8/21 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.6 | 0.018 | 3/8 (LoVo, A549, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.6 | 0.018 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.020 | 5/18 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.46×** | +3.5 | 0.020 | 1/16 (PANC-1) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.5 | 0.020 | 4/20 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.45×** | +3.4 | 0.021 | 1/20 (Hs 766T) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.022 | 4/16 (Hs 766T, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.47×** | +3.3 | 0.029 | 4/15 (HOP62, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.032 | 3/14 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +3.3 | 0.032 | 4/18 (LoVo, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +3.2 | 0.037 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.039 | 7/18 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.049 | 2/14 (A549, NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.39×** | +3.0 | 0.057 | 3/20 (LoVo, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15732.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0846×, RKO 0.104×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.222×); [[Decitabine (drug)]] 0.05 µM in 1 line (RKO 0.0889×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | **0.617×** | -4.4 | 0.007 | 7/21 (Hs 766T, C-33 A, …) | top dose only |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.686× | -3.3 | 0.21 | 0/21 | inconsistent across doses |  |
| [[Perindopril (erbumine) (drug)]] 0.5 µM |  | 0.708× | -3.3 | 0.21 | 3/21 (COLO 205, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 9.47 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -9.4) |
| [[Hs 766T (line)]] | wt | 31.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0846× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 7.21 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0698× (z -8.6) |
| [[A-172 (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.834 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCND3]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SLCO3A1]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[DOK5]] | +0.54 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[MOB3C]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[AFAP1L2]] | +0.52 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[GUCY1A1]] | +0.52 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CFAP46]] | +0.51 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[NEURL1]] | +0.51 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ERG]] | +0.51 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[NHSL2]] | +0.50 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[NECTIN1]] | +0.50 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[UNC80]] | +0.50 | +0.43 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCND3]] | B | KCND3 activity raises DOC2B's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.38× lower at baseline in the lines without KCND3 | 0.061 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[TMEM229B]] | C | TMEM229B activity lowers DOC2B's level | lines that do not express TMEM229B (3) vs lines expressing it (47) | 5.62× higher at baseline in the lines without TMEM229B | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.286). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.5, 38.4); signed map (34.3, 22.7). **Vector** length 37.7, 6.93% of its response variance represented; |z| ≥ 3 in 532 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.2 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.7 | -2.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | double C2 domain beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:142,789-181,650 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DOC2BL |
| Gene groups (HGNC) | Synaptotagmin like tandem C2 proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14184](https://www.uniprot.org/uniprotkb/Q14184) (Double C2-like domain-containing protein beta):

> Calcium sensor which positively regulates SNARE-dependent fusion of vesicles with membranes. Binds phospholipids in a calcium-dependent manner and may act at the priming stage of fusion by modifying membrane curvature to stimulate fusion. Involved in calcium-triggered exocytosis in chromaffin cells and calcium-dependent spontaneous release of neurotransmitter in absence of action potentials in neuronal cells. Involved both in glucose-stimulated insulin secretion in pancreatic cells and …

**Summary**, from NCBI Gene [8447](https://www.ncbi.nlm.nih.gov/gene/8447):

> There are at least two protein isoforms of the Double C2 protein, namely alpha (DOC2A) and beta (DOC2B), which contain two C2-like domains. DOC2A and DOC2B are encoded by different genes; these genes are at times confused with the unrelated DAB2 gene which was initially named DOC-2. DOC2B is expressed ubiquitously and is suggested to be involved in Ca(2+)-dependent intracellular vesicle trafficking in various types of cells. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2986) · Entrez [8447](https://www.ncbi.nlm.nih.gov/gene/8447) · UniProt [Q14184](https://www.uniprot.org/uniprotkb/Q14184) · Ensembl [ENSG00000272636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272636)

## Data

Gene col 15732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15732); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15732]; `tensor/DDL_lfc|DDL_z.npy` [15732]; `embed/gene_vectors.npy` [15732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15732 or target_col == 15732). Every well: [[DOC2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOC2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
