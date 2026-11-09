---
symbol: "CRTC2"
type: "gene"
col: 8374
ensembl_id: "ENSG00000160741"
name: "CREB regulated transcription coactivator 2"
location: "1q21.3"
module: 138
arm: "+"
pooled_cpm: 19.13
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# CRTC2

*CREB regulated transcription coactivator 2* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.96× (z +17.2, q 0e+00, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.0840×; ⚠ toxic; cell-cycle shift, explains ~6% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (H4 0.0897×; ⚠ cell-cycle shift, explains ~0% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.0968×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEPSIN]] (+0.67, fdr 7e-06), [[SORBS3]] (+0.65, fdr 1e-05), [[RIPOR1]] (+0.65, fdr 7e-06).
> It is in [[Module 138]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.96×** | +17.2 | 0e+00 | 45/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.08×** | +8.7 | 1e-15 | 43/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.7 | 2e-12 | 38/46 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +7.5 | 9e-12 | 33/46 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +7.2 | 6e-11 | 29/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +6.8 | 7e-10 | 36/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.6 | 2e-06 | 30/44 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +5.5 | 2e-06 | 28/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +5.2 | 1e-05 | 27/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.003 | 17/46 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +3.7 | 0.011 | 17/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +3.5 | 0.026 | 16/44 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.056 | 14/47 (SNU-423, A498, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.056 | 12/47 (A498, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.059 | 15/47 (PANC-1, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8374.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.0840×; ⚠ toxic; cell-cycle shift, explains ~6% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (H4 0.0897×; ⚠ cell-cycle shift, explains ~0% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.0968×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.744× | -3.5 | 0.17 | 20/47 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | 0.756× | -3.3 | 0.17 | 19/47 (SNU-423, A549, …) | inconsistent across doses | position effect removed |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.757× | -3.3 | 0.17 | 15/46 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.811× | -3.2 | 0.18 | 14/48 (SW 1271, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.768× | -3.2 | 0.18 | 18/47 (SNU-423, SW 1271, …) | rises with dose | position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.823× | -3.1 | 0.20 | 16/48 (C32, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.42× (z +20.5) | — |
| [[SW480 (line)]] | alt | 13.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +9.1) | — |
| [[A-172 (line)]] | wt | 23.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +16.7) | — |
| [[A498 (line)]] | wt | 26.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 9.59 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +12.9) | — |
| [[A549 (line)]] | wt | 14.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0840× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~6% of this change |
| [[CFPAC-1 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +15.7) | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0897× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +9.3) | — |
| [[J82 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +12.7) | — |
| [[LoVo (line)]] | wt | 13.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.74× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +14.0) | — |
| [[NCI-H1792 (line)]] | alt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 42.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 25.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +12.2) | — |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0968× (z -8.5) |
| [[SNU-423 (line)]] | alt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +13.1) | — |
| [[SW48 (line)]] | wt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +9.1) | — |
| [[A-427 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEPSIN]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SORBS3]] | +0.65 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[RIPOR1]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SLC4A2]] | +0.64 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[INPPL1]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ATN1]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[GET4]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[USP19]] | +0.62 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[FBRS]] | +0.61 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[ZBED6]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CTDSP2]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[DVL2]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.815). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, -23.1); signed map (4.6, -8.0). **Vector** length 75.5, 15.2% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +17.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.1 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +0.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.1 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.0 | -3.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | CREB regulated transcription coactivator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,947,669-153,958,615 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TORC2 |
| Reactome | 8 pathways, smallest: Expression of BMAL (ARNTL), CLOCK, and NPAS2; Heme signaling; Transcriptional activation of mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53ET0](https://www.uniprot.org/uniprotkb/Q53ET0) (CREB-regulated transcription coactivator 2):

> Transcriptional coactivator for CREB1 which activates transcription through both consensus and variant cAMP response element (CRE) sites. Acts as a coactivator, in the SIK/TORC signaling pathway, being active when dephosphorylated and acts independently of CREB1 'Ser-133' phosphorylation. Enhances the interaction of CREB1 with TAF4. Regulates gluconeogenesis as a component of the LKB1/AMPK/TORC2 signaling pathway. Regulates the expression of specific genes such as the steroidogenic gene, StAR. …

**Summary**, from NCBI Gene [200186](https://www.ncbi.nlm.nih.gov/gene/200186):

> This gene encodes a member of the transducers of regulated cAMP response element-binding protein activity family of transcription coactivators. These proteins promote the transcription of genes targeted by the cAMP response element-binding protein, and therefore play an important role in many cellular processes. Under basal conditions the encoded protein is phosphorylated by AMP-activated protein kinase or the salt-inducible kinases and is sequestered in the cytoplasm. Upon activation by …

**Accessions** — [HGNC:27301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27301) · Entrez [200186](https://www.ncbi.nlm.nih.gov/gene/200186) · UniProt [Q53ET0](https://www.uniprot.org/uniprotkb/Q53ET0) · Ensembl [ENSG00000160741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160741)

## Data

Gene col 8374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8374); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8374]; `tensor/DDL_lfc|DDL_z.npy` [8374]; `embed/gene_vectors.npy` [8374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8374 or target_col == 8374). Every well: [[CRTC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRTC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
