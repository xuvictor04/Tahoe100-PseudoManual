---
symbol: "NAGPA"
type: "gene"
col: 2330
ensembl_id: "ENSG00000103174"
name: "N-acetylglucosamine-1-phosphodiester alpha-N-acetylglucosaminidase"
location: "16p13.3"
module: 122
arm: "+"
pooled_cpm: 3.78
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# NAGPA

*N-acetylglucosamine-1-phosphodiester alpha-N-acetylglucosaminidase* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.22× (z +8.1, q 3e-13, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.45× (z +5.6, q 4e-06, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.526× (z -9.7, q 2e-19, down in 26 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD9]] (+0.70, fdr 1e-05), [[GLB1]] (+0.66, fdr 1e-05), [[SLC25A38]] (+0.65, fdr 7e-06); moves opposite to [[CCNYL1]] (-0.59, fdr 1e-05), [[ZNF217]] (-0.58, fdr 4e-05), [[CALM2]] (-0.58, fdr 3e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2330.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +8.1 | 3e-13 | 4/5 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +7.6 | 7e-12 | 14/19 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +7.3 | 5e-11 | 5/9 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +5.6 | 4e-06 | 12/46 (RKO, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.5 | 4e-06 | 9/23 (SW480, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +5.1 | 3e-05 | 17/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +4.3 | 0.001 | 13/42 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.014 | 7/46 (HepG2/C3A, KATO III, …) | rises with dose | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.7 | 0.014 | 5/39 (PANC-1, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.4 | 0.032 | 3/14 (KATO III, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.83×** | +3.4 | 0.041 | 3/33 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.066 | 3/46 (LoVo, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.52× | +3.0 | 0.12 | 4/41 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2330.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.526×** | -9.7 | 2e-19 | 26/38 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.444×** | -8.3 | 2e-14 | 30/44 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.608×** | -7.5 | 1e-11 | 26/45 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -7.2 | 8e-11 | 21/38 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.595×** | -5.5 | 3e-06 | 18/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.606×** | -5.4 | 8e-06 | 20/43 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.686×** | -4.0 | 0.005 | 14/47 (C-33 A, HCT15, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.522×** | -3.6 | 0.020 | 9/28 (SW1417, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.538×** | -3.5 | 0.033 | 9/31 (NCI-H23, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.738×** | -3.3 | 0.065 | 13/44 (SNU-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.735× | -3.0 | 0.12 | 9/35 (A498, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.76 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 3.90 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -9.4) |
| [[A-427 (line)]] | wt | 7.12 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.127× (z -9.4) ⚠ transcription drop |
| [[A498 (line)]] | wt | 3.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0791× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 3.19 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0895× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 2.97 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0825× (z -8.8) |
| [[LS 180 (line)]] | wt | 4.15 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0688× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 5.77 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0612× (z -11.8) |
| [[PANC-1 (line)]] | alt | 3.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -8.7) |
| [[RKO (line)]] | wt | 4.38 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0641× (z -8.8) |
| [[A-172 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD9]] | +0.70 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[GLB1]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[SLC25A38]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[GNPTG]] | +0.65 | +0.50 / +0.71 | both halves | 1e-05 | STRING 985 |
| [[KPNA6]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[VPS50]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[SPNS1]] | +0.63 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[ADPGK]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[HEXA]] | +0.61 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[GPATCH3]] | +0.61 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[RPUSD4]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[BABAM1]] | +0.59 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL1]] | -0.59 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[ZNF217]] | -0.58 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[CALM2]] | -0.58 | -0.43 / -0.67 | both halves | 3e-05 |  |
| [[SDC4]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[DPF3]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[NOTCH2NLB]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[HIVEP2]] | -0.52 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PFN1]] | -0.51 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[NBPF10]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[SKIL]] | -0.50 | -0.40 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.609). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-13.3, -14.6); signed map (-32.5, -22.4). **Vector** length 54.7, 7.22% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +2.9 |
|  | [[NG25 (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.4 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | N-acetylglucosamine-1-phosphodiester alpha-N-acetylglucosaminidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:5,024,844-5,034,141 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APAA, UCE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK23](https://www.uniprot.org/uniprotkb/Q9UK23) (N-acetylglucosamine-1-phosphodiester alpha-N-acetylglucosaminidase):

> Catalyzes the second step in the formation of the mannose 6-phosphate targeting signal on lysosomal enzyme oligosaccharides by removing GlcNAc residues from GlcNAc-alpha-P-mannose moieties, which are formed in the first step. Also hydrolyzes UDP-GlcNAc, a sugar donor for Golgi N-acetylglucosaminyltransferases.

**Summary**, from NCBI Gene [51172](https://www.ncbi.nlm.nih.gov/gene/51172):

> Hydrolases are transported to lysosomes after binding to mannose 6-phosphate receptors in the trans-Golgi network. This gene encodes the enzyme that catalyzes the second step in the formation of the mannose 6-phosphate recognition marker on lysosomal hydrolases. Commonly known as 'uncovering enzyme' or UCE, this enzyme removes N-acetyl-D-glucosamine (GlcNAc) residues from GlcNAc-alpha-P-mannose moieties and thereby produces the recognition marker. The encoded preproprotein is proteolytically …

**Accessions** — [HGNC:17378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17378) · Entrez [51172](https://www.ncbi.nlm.nih.gov/gene/51172) · UniProt [Q9UK23](https://www.uniprot.org/uniprotkb/Q9UK23) · Ensembl [ENSG00000103174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103174)

## Data

Gene col 2330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2330); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2330]; `tensor/DDL_lfc|DDL_z.npy` [2330]; `embed/gene_vectors.npy` [2330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2330 or target_col == 2330). Every well: [[NAGPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAGPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
