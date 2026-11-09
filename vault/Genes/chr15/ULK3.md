---
symbol: "ULK3"
type: "gene"
col: 6416
ensembl_id: "ENSG00000140474"
name: "unc-51 like kinase 3"
location: "15q24.1"
module: 2
arm: "+"
pooled_cpm: 6.03
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ULK3

*unc-51 like kinase 3* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.97× (z +8.5, q 2e-14, up in 6 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.68× (z +4.8, q 2e-04, up in 12 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.372× (z -6.7, q 1e-08, down in 22 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM65]] (+0.63, fdr 1e-05), [[FAM219B]] (+0.62, fdr 1e-05), [[MAN2A2]] (+0.62, fdr 7e-06); moves opposite to [[XRN1]] (-0.47, fdr 8e-05), [[KLHL4]] (-0.47, fdr 9e-05), [[MBD5]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.5 | 2e-14 | 6/11 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.9 | 2e-09 | 15/28 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +6.8 | 3e-09 | 15/31 (NCI-H460, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +6.2 | 1e-07 | 6/17 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.8 | 7e-07 | 12/32 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +4.8 | 2e-04 | 12/35 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 8e-04 | 9/36 (LoVo, SW1417, …) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 8e-04 | 9/43 (LS 180, A549, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.0 | 0.003 | 6/16 (HT-29, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.021 | 7/47 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.032 | 4/42 (A498, hTERT-HPNE, …) | two highest doses |  |
| [[Pimitespib (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.055 | 3/29 (LOX-IMVI, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ritonavir (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.084 | 6/44 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.18× | +3.1 | 0.086 | 4/46 (C32, A498, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6416.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.372×** | -6.7 | 1e-08 | 22/45 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.482×** | -5.0 | 2e-04 | 15/41 (BT-474, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.710×** | -4.5 | 0.002 | 15/47 (SW1417, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.739×** | -4.0 | 0.011 | 16/45 (HepG2/C3A, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.752×** | -3.7 | 0.022 | 11/47 (LOX-IMVI, SW48, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.825×** | -3.6 | 0.034 | 16/40 (NCI-H2030, SW48, …) | rises with dose | composition shift |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.768×** | -3.5 | 0.045 | 8/44 (J82, AN3 CA, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.778×** | -3.3 | 0.073 | 9/47 (HOP62, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.780×** | -3.2 | 0.073 | 9/46 (KATO III, NCI-H2030, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.782×** | -3.2 | 0.075 | 9/42 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.785×** | -3.2 | 0.079 | 10/41 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 6.52 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0964× (z -8.9) ⚠ transcription drop · without an alert: [[Vandetanib (drug)]] 0.5 µM 0.107× (z -8.5) |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0970× (z -9.1) |
| [[C32 (line)]] | wt | 5.21 | 0 | 1 | — | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM 0.0779× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 5.85 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0661× (z -12.2) |
| [[HS-578T (line)]] | alt | 4.64 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0517× (z -11.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 6.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -9.1) |
| [[RKO (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0859× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 5.79 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0615× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 6.49 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0776× (z -9.7) |
| [[SW480 (line)]] | alt | 5.08 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM65]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[FAM219B]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 | STRING 569 |
| [[MAN2A2]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[NDST2]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[GRK2]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 | pathway: Hedgehog 'on' state |
| [[INTS15]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NBEAL2]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[PLA2G4B]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[FHIP2B]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[VARS2]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRN1]] | -0.47 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[KLHL4]] | -0.47 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[MBD5]] | -0.45 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[GPBP1]] | -0.44 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[SRP14]] | -0.44 | -0.47 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-11.2, -23.8); signed map (-25.4, -1.1). **Vector** length 50.4, 5.79% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +8.5 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.3 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +4.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +1.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +4.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.4 | -6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | unc-51 like kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:74,836,118-74,843,346 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434C131, FLJ90566 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Unc-51 like kinase family |
| Reactome | 2 pathways, smallest: Hedgehog 'on' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PHR2](https://www.uniprot.org/uniprotkb/Q6PHR2) (Serine/threonine-protein kinase ULK3):

> Serine/threonine protein kinase that acts as a regulator of smoothened signaling and autophagy. Acts as a positive regulator of smoothened signaling in the presence of hedgehog (DHH, IHH or SHH) ligand: autophosphorylates and mediates phosphorylation of full-length GLI2, promoting subsequent phosphorylation by CDK1 and GLI2 dissociation from SUFU and translocation to the nucleus. Also phosphorylates as GLI1 and GLI3, although less efficiently. In the absence of hedgehog ligand, interacts with …

**Summary**, from NCBI Gene [25989](https://www.ncbi.nlm.nih.gov/gene/25989):

> Enables protein serine/threonine kinase activity. Involved in several processes, including fibroblast activation; protein autophosphorylation; and regulation of smoothened signaling pathway. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19703) · Entrez [25989](https://www.ncbi.nlm.nih.gov/gene/25989) · UniProt [Q6PHR2](https://www.uniprot.org/uniprotkb/Q6PHR2) · Ensembl [ENSG00000140474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140474)

## Data

Gene col 6416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6416); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6416]; `tensor/DDL_lfc|DDL_z.npy` [6416]; `embed/gene_vectors.npy` [6416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6416 or target_col == 6416). Every well: [[ULK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ULK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
