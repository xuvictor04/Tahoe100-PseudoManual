---
symbol: "SYN1"
type: "gene"
col: 157
ensembl_id: "ENSG00000008056"
name: "synapsin I"
location: "Xp11.3-p11.23"
module: 61
arm: "+"
pooled_cpm: 2.32
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# SYN1

*synapsin I* — Xp11.3-p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.95× (z +14.7, q 0e+00, up in 20 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTUS2]] (+0.71, fdr 1e-05), [[CAMK2B]] (+0.70, fdr 7e-06), [[CELF5]] (+0.69, fdr 1e-05); moves opposite to [[TCEANC2]] (-0.57, fdr 4e-05), [[ANGEL2]] (-0.55, fdr 3e-05), [[QRSL1]] (-0.54, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GAP43]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.95×** | +14.7 | 0e+00 | 20/32 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.14×** | +13.6 | 9e-40 | 31/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.95×** | +13.2 | 2e-37 | 26/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.54×** | +12.6 | 2e-34 | 27/43 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.08×** | +10.8 | 5e-25 | 22/41 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +10.2 | 3e-22 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.83×** | +10.0 | 1e-21 | 8/11 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +8.0 | 8e-14 | 13/31 (NCI-H2347, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +7.5 | 5e-12 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +6.5 | 3e-09 | 15/37 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.97×** | +6.5 | 5e-09 | 2/11 (PANC-1, RKO) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.95×** | +6.4 | 7e-09 | 19/43 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +5.8 | 2e-07 | 16/37 (A-172, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +3.5 | 0.017 | 5/34 (NCI-H460, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.023 | 7/29 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.043 | 5/45 (NCI-H1792, HS-578T, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.56×** | +3.0 | 0.066 | 0/26 | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +2.9 | 0.099 | 3/22 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 157.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 0.782× | -3.4 | 0.32 | 10/41 (hTERT-HPNE, C32, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.788× | -3.3 | 0.32 | 11/40 (SW 900, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 4.28 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 17.6× (z +14.1) | — |
| [[NCI-H460 (line)]] | wt | 2.86 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 27.9× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 1.65 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 34.8× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 4.17 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 19.3× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 2.01 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 34.7× (z +9.8) | — |
| [[A-172 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTUS2]] | +0.71 | +0.55 / +0.85 | both halves | 1e-05 |  |
| [[CAMK2B]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 | pathway: Neuronal System; STRING 451 |
| [[CELF5]] | +0.69 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[EPHB1]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[VAT1L]] | +0.66 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[ATP1A3]] | +0.66 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[DLGAP2]] | +0.66 | +0.66 / +0.75 | both halves | 7e-06 | pathway: Neuronal System |
| [[KCNN3]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | pathway: Neuronal System |
| [[ALK]] | +0.64 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ARC]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 | STRING 410 |
| [[HS6ST3]] | +0.63 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[PKNOX2]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEANC2]] | -0.57 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ANGEL2]] | -0.55 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[QRSL1]] | -0.54 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[TRAPPC13]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAP43]] | B | GAP43 activity raises SYN1's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without GAP43 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[SYT11]] | B | SYT11 activity raises SYN1's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 1.47× lower at baseline in the lines without SYT11 | 0.036 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[EBF2]] | B | EBF2 activity strengthens SYN1's drug response | lines that do not express EBF2 (17) vs lines expressing it (28) | the lines without EBF2 respond 0.50× as strongly (z diff +1.93); strongest at Belinostat 5 µM: 1.60x vs 4.63x (z diff +3.3) | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SCG3]] | B | SCG3 activity raises SYN1's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 1.46× lower at baseline in the lines without SCG3 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[FSD1]] | B | FSD1 activity raises SYN1's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.40× lower at baseline in the lines without FSD1 | 0.065 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[LINC02885]] | B | LINC02885 activity raises SYN1's level | lines that do not express LINC02885 (15) vs lines expressing it (35) | 1.23× lower at baseline in the lines without LINC02885 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC01399, PCDHB2, ENSG00000258168; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.2, 33.3); signed map (28.3, 20.3). **Vector** length 52.2, 6.89% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +5.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | synapsin I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3-p11.23 — chrX:47,571,901-47,619,857 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MRX50 |
| Gene groups (HGNC) | Synapsins |
| Reactome | 8 pathways, smallest: Serotonin Neurotransmitter Release Cycle; Dopamine Neurotransmitter Release Cycle; Neurotransmitter release cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P17600](https://www.uniprot.org/uniprotkb/P17600) (Synapsin-1):

> Neuronal phosphoprotein that coats synaptic vesicles, and binds to the cytoskeleton. Acts as a regulator of synaptic vesicles trafficking, involved in the control of neurotransmitter release at the pre-synaptic terminal. Also involved in the regulation of axon outgrowth and synaptogenesis (By similarity). The complex formed with NOS1 and CAPON proteins is necessary for specific nitric-oxid functions at a presynaptic level (By similarity).

**Summary**, from NCBI Gene [6853](https://www.ncbi.nlm.nih.gov/gene/6853):

> This gene is a member of the synapsin gene family. Synapsins encode neuronal phosphoproteins which associate with the cytoplasmic surface of synaptic vesicles. Family members are characterized by common protein domains, and they are implicated in synaptogenesis and the modulation of neurotransmitter release, suggesting a potential role in several neuropsychiatric diseases. This member of the synapsin family plays a role in regulation of axonogenesis and synaptogenesis. The protein encoded …

**Accessions** — [HGNC:11494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11494) · Entrez [6853](https://www.ncbi.nlm.nih.gov/gene/6853) · UniProt [P17600](https://www.uniprot.org/uniprotkb/P17600) · Ensembl [ENSG00000008056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008056)

## Data

Gene col 157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 157); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 157]; `tensor/DDL_lfc|DDL_z.npy` [157]; `embed/gene_vectors.npy` [157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 157 or target_col == 157). Every well: [[SYN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
