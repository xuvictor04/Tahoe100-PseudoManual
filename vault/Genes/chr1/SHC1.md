---
symbol: "SHC1"
type: "gene"
col: 8368
ensembl_id: "ENSG00000160691"
name: "SHC adaptor protein 1"
location: "1q21.3"
module: 50
arm: "+"
pooled_cpm: 63.53
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# SHC1

*SHC adaptor protein 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.61× (z +5.7, q 5e-06, up in 29 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dexamethasone (drug)]] 0.5 µM in 3 lines (NCI-H1573 5.04×, NCI-H460 2.73×, Hs 766T 2.95×); [[Dexamethasone (drug)]] 5 µM in 2 lines (NCI-H1573 4.91×, NCI-H460 2.66×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 5.24×).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.671× (z -6.9, q 3e-09, down in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.723× (z -5.6, q 6e-06, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK16]] (+0.63, fdr 7e-06), [[ATP1A1]] (+0.62, fdr 7e-06), [[PSME3]] (+0.62, fdr 1e-05); moves opposite to [[SNHG6]] (-0.54, fdr 2e-05), [[ATP5MC2]] (-0.54, fdr 2e-05), [[SMIM26]] (-0.53, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[TRIM52-AS1]] (-0.52, fdr 1e-04).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8368.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dexamethasone (drug)]] 0.5 µM in 3 lines (NCI-H1573 5.04×, NCI-H460 2.73×, Hs 766T 2.95×); [[Dexamethasone (drug)]] 5 µM in 2 lines (NCI-H1573 4.91×, NCI-H460 2.66×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 5.24×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +5.7 | 5e-06 | 29/47 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +5.1 | 1e-04 | 23/40 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.8 | 4e-04 | 5/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.26 | 20/47 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.29× | +3.0 | 0.26 | 21/48 (RKO, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8368.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.671×** | -6.9 | 3e-09 | 33/47 (RKO, NCI-H23, …) | rises with dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.723×** | -5.6 | 6e-06 | 37/47 (SNU-1, CHP-212, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.716×** | -4.1 | 0.009 | 33/47 (SNU-1, NCI-H23, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **0.737×** | -3.7 | 0.026 | 28/47 (RPMI-7951, A549, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.828× | -3.3 | 0.11 | 21/48 (H4, RKO, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.689× | -3.3 | 0.11 | 25/47 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sulfisoxazole (drug)]] 5 µM |  | 0.835× | -3.1 | 0.14 | 20/47 (SHP-77, C32, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 82.6 | 13 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 5.24× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 190 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -11.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 240 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.294× (z -8.6) |
| [[A-172 (line)]] | wt | 85.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 88.7 | 2 | 0 | [[Dexamethasone (drug)]] 0.5 µM 2.73× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -15.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 145 | 1 | 0 | [[Dexamethasone (drug)]] 0.5 µM 2.95× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -11.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 164 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -20.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 48.6 | 0 | 1 | — | [[ULK-101 (drug)]] 5 µM 0.0613× (z -9.8) |
| [[A-427 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK16]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ATP1A1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PSME3]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PYGO2]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NOP9]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[COPS8]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TTLL12]] | +0.57 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[GPC1]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 | pathway: Cell surface interactions at the vascular wall |
| [[TMEM43]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[LIN7C]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[RAB11B]] | +0.55 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[EMC1]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG6]] | -0.54 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[ATP5MC2]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SMIM26]] ⚠ | -0.53 | -0.49 / -0.50 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCRB]] ⚠ | -0.53 | -0.43 / -0.57 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NACA4P]] ⚠ | -0.53 | -0.43 / -0.52 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRIM52-AS1]] | -0.52 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[SNHG32]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[COX17]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[NSA2]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.51 | -0.37 / -0.51 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5P2-1]] ⚠ | -0.51 | -0.39 / -0.53 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZMYM5]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[BTBD7]] | -0.50 | -0.26 / -0.49 | both halves | 3e-04 |  |
| [[GABARAPL2]] | -0.50 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[MPHOSPH8]] | -0.50 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[TOMM7]] | -0.50 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[RPL36]] | -0.50 | -0.35 / -0.56 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.486). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.4, -29.1); signed map (-8.8, -38.7). **Vector** length 131, 37.3% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dexamethasone (drug)]] 0.5 µM |  | +5.3 | +2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +5.2 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.8 | +2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.3 | +2.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +4.2 | +1.1 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -4.9 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.9 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.6 | -6.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.2 | -1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.8 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | SHC adaptor protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,962,298-154,974,395 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p66, ShcA; previously SHC |
| Gene groups (HGNC) | SH2 domain containing |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, APICAL_JUNCTION |
| Reactome | 93 pathways, smallest: Activated NTRK2 signals through RAS; Activated NTRK3 signals through RAS; SHC-related events triggered by IGF1R |
| Matched by | ensembl_id |

**Function**, from UniProt [P29353](https://www.uniprot.org/uniprotkb/P29353) (SHC-transforming protein 1):

> Signaling adapter that couples activated growth factor receptors to signaling pathways. Participates in a signaling cascade initiated by activated KIT and KITLG/SCF. Isoform p46Shc and isoform p52Shc, once phosphorylated, couple activated receptor tyrosine kinases to Ras via the recruitment of the GRB2/SOS complex and are implicated in the cytoplasmic propagation of mitogenic signals. Isoform p46Shc and isoform p52Shc may thus function as initiators of the Ras signaling cascade in various …

**Summary**, from NCBI Gene [6464](https://www.ncbi.nlm.nih.gov/gene/6464):

> This gene encodes three main isoforms that differ in activities and subcellular location. While all three are adapter proteins in signal transduction pathways, the longest (p66Shc) may be involved in regulating life span and the effects of reactive oxygen species. The other two isoforms, p52Shc and p46Shc, link activated receptor tyrosine kinases to the Ras pathway by recruitment of the GRB2/SOS complex. p66Shc is not involved in Ras activation. Unlike the other two isoforms, p46Shc is targeted …

**Accessions** — [HGNC:10840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10840) · Entrez [6464](https://www.ncbi.nlm.nih.gov/gene/6464) · UniProt [P29353](https://www.uniprot.org/uniprotkb/P29353) · Ensembl [ENSG00000160691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160691)

## Data

Gene col 8368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8368); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8368]; `tensor/DDL_lfc|DDL_z.npy` [8368]; `embed/gene_vectors.npy` [8368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8368 or target_col == 8368). Every well: [[SHC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
