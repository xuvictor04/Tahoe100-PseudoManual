---
symbol: "PSENEN"
type: "gene"
col: 12952
ensembl_id: "ENSG00000205155"
name: "presenilin enhancer, gamma-secretase subunit"
location: "19q13.12"
module: 48
arm: "+"
pooled_cpm: 8.35
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# PSENEN

*presenilin enhancer, gamma-secretase subunit* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.43× (z +8.5, q 8e-15, up in 25 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +5.0, q 6e-05, up in 19 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.626× (z -6.4, q 1e-07, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2G]] (+0.63, fdr 1e-05, ⚠ POLR2G in the vector space only through flagged drug-doses), [[EMC4]] (+0.57, fdr 4e-05), [[TMEM179B]] (+0.56, fdr 2e-05), [[RNASEK]] (+0.52, fdr 1e-05); moves opposite to [[SNHG17]] (-0.58, fdr 1e-05), [[PLA2G4B]] (-0.57, fdr 7e-06), [[PAQR6]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.43×** | +8.5 | 8e-15 | 25/31 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.64×** | +6.6 | 2e-08 | 7/13 (PANC-1, HOP62, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.93×** | +5.9 | 9e-07 | 15/23 (HEC-1-A, NCI-H460, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +5.8 | 9e-07 | 24/39 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.0 | 6e-05 | 19/44 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.67×** | +5.0 | 7e-05 | 25/46 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.54×** | +4.2 | 0.002 | 17/47 (C-33 A, LS 180, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.1 | 0.003 | 15/46 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.0 | 0.005 | 7/48 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Lapatinib ditosylate (drug)]] 0.05 µM |  | **1.46×** | +3.4 | 0.034 | 12/45 (HT-29, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.073 | 5/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.39×** | +3.2 | 0.073 | 17/43 (PANC-1, HEC-1-A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12952.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.626×** | -6.4 | 1e-07 | 29/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.618×** | -4.6 | 0.001 | 29/45 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.661×** | -4.0 | 0.013 | 15/47 (NCI-H661, SNU-423, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.678×** | -3.7 | 0.022 | 13/47 (NCI-H2030, SW 1271, …) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.679×** | -3.7 | 0.022 | 17/47 (J82, LoVo, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.687×** | -3.6 | 0.030 | 19/45 (HEC-1-A, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.709×** | -3.3 | 0.075 | 12/46 (PANC-1, A549, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.718× | -3.2 | 0.10 | 12/47 (BT-474, A498, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 0.5 µM |  | 0.722× | -3.1 | 0.11 | 11/47 (HS-578T, SW 900, …) | inconsistent across doses |  |
| [[Altretamine (drug)]] 0.5 µM |  | 0.729× | -3.0 | 0.13 | 9/46 (hTERT-HPNE, A549, …) | inconsistent across doses |  |
| [[olaparib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.730× | -3.0 | 0.13 | 5/47 (PANC-1, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 12.7 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0945× (z -8.5) |
| [[PANC-1 (line)]] | alt | 15.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2G]] ⚠ | +0.63 | +0.63 / +0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EMC4]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[TMEM179B]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[RNASEK]] | +0.52 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ARF5]] | +0.51 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[PPP1R7]] | +0.50 | +0.29 / +0.59 | both halves | 3e-04 |  |
| [[GET3]] | +0.50 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[SP1]] | +0.49 | +0.45 / +0.53 | both halves | 3e-05 | pathway: Signaling by TGFB family members |
| [[BLOC1S1]] | +0.49 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[PPP1CA]] | +0.49 | +0.41 / +0.49 | both halves | 4e-05 | pathway: Signaling by TGFB family members |
| [[GRN]] | +0.49 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[TMED1]] | +0.48 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[PDZD11]] | +0.48 | +0.35 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG17]] | -0.58 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[PLA2G4B]] | -0.57 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[PAQR6]] | -0.50 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[AGER]] | -0.47 | -0.47 / -0.35 | both halves | 1e-04 | STRING 418 |
| [[OPLAH]] ⚠ | -0.47 | -0.50 / -0.39 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CPNE7]] | -0.47 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[NOP58]] | -0.46 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CTBP1]] | -0.46 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[PNN]] | -0.46 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[MTA1]] | -0.46 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[KAT2A]] | -0.45 | -0.50 / -0.36 | both halves | 9e-05 | pathway: HALLMARK_NOTCH_SIGNALING |
| [[ZNF692]] | -0.44 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[FAAH]] | -0.44 | -0.37 / -0.41 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.281). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-21.3, -47.2); signed map (-20.8, -3.3). **Vector** length 66.4, 12.3% of its response variance represented; |z| ≥ 3 in 677 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.7 | +3.2 |
|  | [[Thymol (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | presenilin enhancer, gamma-secretase subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,745,600-35,747,519 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEN2 |
| Gene groups (HGNC) | Gamma-secretase complex subunits |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 33 pathways, smallest: Noncanonical activation of NOTCH3; NOTCH4 Activation and Transmission of Signal to the Nucleus; Regulated proteolysis of p75NTR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ42](https://www.uniprot.org/uniprotkb/Q9NZ42) (Gamma-secretase subunit PEN-2):

> Essential subunit of the gamma-secretase complex, an endoprotease complex that catalyzes the intramembrane cleavage of integral membrane proteins such as Notch receptors and APP (amyloid-beta precursor protein). The gamma-secretase complex plays a role in Notch and Wnt signaling cascades and regulation of downstream processes via its role in processing key regulatory proteins, and by regulating cytosolic CTNNB1 levels (Probable). PSENEN modulates both endoproteolysis of presenilin and …

**Summary**, from NCBI Gene [55851](https://www.ncbi.nlm.nih.gov/gene/55851):

> Presenilins, which are components of the gamma-secretase protein complex, are required for intramembranous processing of some type I transmembrane proteins, such as the Notch proteins and the beta-amyloid precursor protein. Signaling by Notch receptors mediates a wide range of developmental cell fates. Processing of the beta-amyloid precursor protein generates neurotoxic amyloid beta peptides, the major component of senile plaques associated with Alzheimer's disease. This gene encodes a protein …

**Accessions** — [HGNC:30100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30100) · Entrez [55851](https://www.ncbi.nlm.nih.gov/gene/55851) · UniProt [Q9NZ42](https://www.uniprot.org/uniprotkb/Q9NZ42) · Ensembl [ENSG00000205155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205155)

## Data

Gene col 12952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12952); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12952]; `tensor/DDL_lfc|DDL_z.npy` [12952]; `embed/gene_vectors.npy` [12952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12952 or target_col == 12952). Every well: [[PSENEN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSENEN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
