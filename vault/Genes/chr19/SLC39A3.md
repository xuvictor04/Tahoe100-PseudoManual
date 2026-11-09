---
symbol: "SLC39A3"
type: "gene"
col: 6578
ensembl_id: "ENSG00000141873"
name: "solute carrier family 39 member 3"
location: "19p13.3"
module: 58
arm: "+"
pooled_cpm: 3.11
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# SLC39A3

*solute carrier family 39 member 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.59× (z +14.0, q 2e-41, up in 44 of 46 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.36× (z +7.9, q 5e-13, up in 30 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.662× (z -5.3, q 5e-05, down in 23 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HS-578T 0.0795×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (J82 0.0815×); [[Tazarotene (drug)]] 0.5 µM in 1 line (LoVo 0.0720×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WRAP73]] (+0.69, fdr 6e-05), [[RPUSD1]] (+0.68, fdr 3e-05), [[ANTKMT]] (+0.67, fdr 3e-05); moves opposite to [[LHFPL3]] (-0.70, fdr 3e-05), [[TPTE2P6]] (-0.64, fdr 4e-05), [[KMT2E-AS1]] (-0.64, fdr 1e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **4.59×** | +14.0 | 2e-41 | 44/46 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **4.35×** | +13.5 | 8e-39 | 41/43 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.67×** | +9.0 | 5e-17 | 35/45 (SW480, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.57×** | +8.2 | 3e-14 | 2/5 (NCI-H2030, A498) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.36×** | +7.9 | 5e-13 | 30/40 (SW480, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **2.07×** | +6.7 | 3e-09 | 7/15 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +6.5 | 5e-09 | 15/20 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.97×** | +6.2 | 4e-08 | 7/17 (SW1417, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.85×** | +5.2 | 1e-05 | 3/7 (SW1417, A498, …) | all doses, stronger at high dose | composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.0 | 0.003 | 1/8 (PANC-1) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.55×** | +4.0 | 0.003 | 10/47 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +3.9 | 0.004 | 8/47 (NCI-H1792, SW 900, …) | inconsistent across doses | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.9 | 0.005 | 6/30 (J82, SHP-77, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **1.51×** | +3.6 | 0.014 | 7/26 (NCI-H460, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +3.6 | 0.014 | 13/35 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM |  | **1.71×** | +3.2 | 0.050 | 0/30 | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.068 | 4/31 (SHP-77, C-33 A, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.64×** | +2.9 | 0.100 | 1/34 (J82) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6578.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HS-578T 0.0795×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (J82 0.0815×); [[Tazarotene (drug)]] 0.5 µM in 1 line (LoVo 0.0720×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -5.3 | 5e-05 | 23/34 (NCI-H460, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.625×** | -4.1 | 0.012 | 13/37 (HS-578T, Panc 03.27, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.711× | -3.1 | 0.30 | 11/38 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.527× | -3.1 | 0.30 | 5/43 (SW480, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 5.36 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0795× (z -9.0) |
| [[J82 (line)]] | alt | 3.94 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0815× (z -8.7) |
| [[LoVo (line)]] | wt | 2.31 | 0 | 1 | — | [[Tazarotene (drug)]] 0.5 µM 0.0720× (z -8.5) |
| [[A-172 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | +0.69 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[RPUSD1]] | +0.68 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[ANTKMT]] | +0.67 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[PUSL1]] | +0.67 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[SNRNP25]] | +0.66 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CBR1]] | +0.65 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[NAA40]] | +0.65 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[STUB1]] | +0.64 | +0.43 / +0.36 | both halves | 1e-04 |  |
| [[RRP1B]] | +0.64 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[DCTPP1]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[KCTD17]] | +0.62 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[POLR3B]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LHFPL3]] | -0.70 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[TPTE2P6]] | -0.64 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[KMT2E-AS1]] | -0.64 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[ANXA4]] | -0.63 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ZNF451-AS1]] | -0.62 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[HOXB-AS3]] | -0.61 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[N4BP2L1]] | -0.61 | -0.52 / -0.24 | both halves | 5e-04 |  |
| [[AP4S1]] | -0.61 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[EYS]] | -0.61 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[CCDC17]] | -0.61 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[PPP1R12A-AS2]] | -0.61 | -0.35 / -0.23 | both halves | 5e-04 |  |
| [[OARD1]] | -0.60 | -0.36 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.596). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.5, 19.6); signed map (-31.5, 2.7). **Vector** length 52.6, 7.33% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.9 | +13.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.7 | +14.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +7.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.1 | +9.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +1.5 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.0 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +2.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -0.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 39 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,732,204-2,740,028 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZIP3 |
| Gene groups (HGNC) | Solute carrier family 39 |
| Reactome | 5 pathways, smallest: Zinc influx into cells by the SLC39 gene family; Zinc transporters; Metal ion SLC transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRY0](https://www.uniprot.org/uniprotkb/Q9BRY0) (Zinc transporter ZIP3):

> Transporter for the divalent cation Zn(2+). Mediates the influx of Zn(2+) into cells from extracellular space. Controls Zn(2+) accumulation into dentate gyrus granule cells in the hippocampus. Mediates Zn(2+) reuptake from the secreted milk within the alveolar lumen.

**Summary**, from NCBI Gene [29985](https://www.ncbi.nlm.nih.gov/gene/29985):

> Predicted to enable zinc ion transmembrane transporter activity. Predicted to be involved in zinc ion transmembrane transport. Predicted to act upstream of or within several processes, including T cell homeostasis; chordate embryonic development; and zinc ion transport. Predicted to be located in hippocampal mossy fiber to CA3 synapse. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17128) · Entrez [29985](https://www.ncbi.nlm.nih.gov/gene/29985) · UniProt [Q9BRY0](https://www.uniprot.org/uniprotkb/Q9BRY0) · Ensembl [ENSG00000141873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141873)

## Data

Gene col 6578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6578); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6578]; `tensor/DDL_lfc|DDL_z.npy` [6578]; `embed/gene_vectors.npy` [6578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6578 or target_col == 6578). Every well: [[SLC39A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC39A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
