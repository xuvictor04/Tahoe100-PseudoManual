---
symbol: "COPS7A"
type: "gene"
col: 3251
ensembl_id: "ENSG00000111652"
name: "COP9 signalosome subunit 7A"
location: "12p13.31"
module: 127
arm: "+"
pooled_cpm: 14.07
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# COPS7A

*COP9 signalosome subunit 7A* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.55× (z +17.7, q 0e+00, up in 26 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.49× (z +3.4, q 0.064, up in 6 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.597× (z -10.6, q 2e-23, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POFUT1]] (+0.62, fdr 1e-05), [[TTC14]] (+0.59, fdr 5e-05), [[EMC1]] (+0.57, fdr 2e-05); moves opposite to [[ING2]] (-0.54, fdr 6e-05), [[LINC02362]] (-0.51, fdr 3e-05), [[MSX1]] (-0.49, fdr 7e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3251.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.55×** | +17.7 | 0e+00 | 26/26 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +16.1 | 0e+00 | 33/36 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +10.1 | 1e-21 | 27/33 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.37×** | +4.6 | 8e-04 | 19/44 (SNU-423, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.0 | 0.008 | 8/30 (CFPAC-1, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.058 | 12/48 (A-427, A-172, …) | top dose only | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.064 | 6/42 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.096 | 13/43 (Panc 03.27, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.096 | 12/46 (LOX-IMVI, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3251.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.597×** | -10.6 | 2e-23 | 35/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.691×** | -5.4 | 2e-05 | 24/46 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.685×** | -5.3 | 3e-05 | 24/47 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.742×** | -4.3 | 0.002 | 19/47 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -4.2 | 0.003 | 22/46 (RKO, HCT15, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.753×** | -4.1 | 0.004 | 20/48 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.802× | -3.1 | 0.15 | 16/46 (NCI-H460, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.809× | -3.1 | 0.15 | 12/47 (A549, C32, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 15.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -8.8) |
| [[PANC-1 (line)]] | alt | 13.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.0) |
| [[A498 (line)]] | wt | 14.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 16.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.9) |
| [[SW480 (line)]] | alt | 18.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +12.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 12.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 10.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.232× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~51% of this change |
| [[KATO III (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +8.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -16.7) |
| [[NCI-H1792 (line)]] | alt | 9.72 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.88× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -8.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.79× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.20× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POFUT1]] | +0.62 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TTC14]] | +0.59 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[EMC1]] | +0.57 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[SNRNP200]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[VTI1B]] | +0.56 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[FAM91A1]] | +0.56 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[MRPL3]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PABIR2]] | +0.55 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[EFTUD2]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[AGO1]] | +0.54 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[MRPL42]] | +0.54 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[SPATA20]] | +0.54 | +0.34 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING2]] | -0.54 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[LINC02362]] | -0.51 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[MSX1]] | -0.49 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[FOXC1]] | -0.49 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[PHLPP2]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[IRX5]] | -0.47 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[PSMD6-AS2]] | -0.47 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[CBR3]] | -0.47 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[PSME2]] | -0.47 | -0.43 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.9, -15.1); signed map (-31.4, -26.6). **Vector** length 44.6, 5.47% of its response variance represented; |z| ≥ 3 in 686 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +17.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +10.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.0 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -10.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.5 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.0 | -5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.7 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -0.7 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.6 | -0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | COP9 signalosome subunit 7A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,724,014-6,731,875 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CSN7A |
| Gene groups (HGNC) | COP9 signalosome |
| Reactome | 11 pathways, smallest: DNA Damage Recognition in GG-NER; Formation of TC-NER Pre-Incision Complex; Transcription-Coupled Nucleotide Excision Repair (TC-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBW8](https://www.uniprot.org/uniprotkb/Q9UBW8) (COP9 signalosome complex subunit 7a):

> Component of the COP9 signalosome (CSN), a master regulator of the ubiquitin conjugation pathway. CSN mediates the deneddylation of the cullin subunits of all cullin-RING ligases. By reversing the activating neddylation on the cullin-RING ligase, the COP9 signalosome restores the ligase to its inactive state and resets it for substrate recognition. CSN is also involved in phosphorylation of p53/TP53, c-jun/JUN, IkappaBalpha/NFKBIA, ITPK1 and IRF8/ICSBP, possibly via its association with CK2 and …

**Summary**, from NCBI Gene [50813](https://www.ncbi.nlm.nih.gov/gene/50813):

> This gene encodes a component of the COP9 signalosome, an evolutionarily conserved multi-subunit protease that regulates the activity of the ubiquitin conjugation pathway. Alternatively spliced transcript variants that encode the same protein have been described. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:16758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16758) · Entrez [50813](https://www.ncbi.nlm.nih.gov/gene/50813) · UniProt [Q9UBW8](https://www.uniprot.org/uniprotkb/Q9UBW8) · Ensembl [ENSG00000111652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111652)

## Data

Gene col 3251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3251); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3251]; `tensor/DDL_lfc|DDL_z.npy` [3251]; `embed/gene_vectors.npy` [3251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3251 or target_col == 3251). Every well: [[COPS7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPS7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
