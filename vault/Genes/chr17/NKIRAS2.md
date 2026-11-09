---
symbol: "NKIRAS2"
type: "gene"
col: 9618
ensembl_id: "ENSG00000168256"
name: "NFKB inhibitor interacting Ras like 2"
location: "17q21.2"
module: 7
arm: "+"
pooled_cpm: 18.29
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# NKIRAS2

*NFKB inhibitor interacting Ras like 2* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.07× (z +8.9, q 3e-16, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.644× (z -5.4, q 4e-05, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (COLO 205 0.206×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0897×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL10]] (+0.65, fdr 1e-05), [[ZNF426]] (+0.63, fdr 7e-06), [[MED7]] (+0.62, fdr 7e-06); moves opposite to [[RANBP1]] (-0.58, fdr 1e-05), [[TBC1D4]] (-0.55, fdr 1e-05), [[CDCA7]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.07×** | +8.9 | 3e-16 | 43/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.93×** | +7.8 | 2e-12 | 32/41 (J82, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +7.2 | 1e-10 | 38/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +7.1 | 2e-10 | 39/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +7.0 | 3e-10 | 37/47 (A-172, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.80×** | +6.9 | 4e-10 | 22/27 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.7 | 2e-04 | 21/45 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.004 | 23/46 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.009 | 18/48 (A-172, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.040 | 12/46 (A498, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.3 | 0.054 | 18/43 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.058 | 14/47 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.2 | 0.071 | 15/38 (HS-578T, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.074 | 18/47 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.1 | 0.080 | 7/30 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9618.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (COLO 205 0.206×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0897×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.644×** | -5.4 | 4e-05 | 28/47 (COLO 205, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.753× | -3.5 | 0.11 | 18/47 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.755× | -3.4 | 0.11 | 20/48 (COLO 205, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.760× | -3.4 | 0.11 | 16/47 (KATO III, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | 0.768× | -3.1 | 0.21 | 13/47 (hTERT-HPNE, Panc 03.27, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.206× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 22.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.12× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0897× (z -8.5) |
| [[SW480 (line)]] | alt | 16.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.78× (z +8.5) | — |
| [[A-172 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL10]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ZNF426]] | +0.63 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[MED7]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[POP4]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[TOX4]] | +0.61 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[RBSN]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 | pathway: Toll Like Receptor 9 (TLR9) Cascade |
| [[EXOC8]] | +0.60 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[ELOF1]] | +0.59 | +0.68 / +0.38 | both halves | 6e-05 |  |
| [[KIF3B]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[WBP2]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[PEX16]] | +0.59 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[UCK1]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP1]] | -0.58 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[TBC1D4]] | -0.55 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[CDCA7]] | -0.53 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[EZH2]] | -0.53 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[HELLS]] | -0.51 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[LMNB1]] | -0.50 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ELOVL6]] | -0.50 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[ARGLU1]] | -0.49 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[ZNF367]] | -0.49 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[FANCC]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.537). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.6, -3.7); signed map (-9.1, -8.3). **Vector** length 63.0, 11.3% of its response variance represented; |z| ≥ 3 in 694 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | +7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | +8.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.2 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | NFKB inhibitor interacting Ras like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,011,382-42,025,644 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KBRAS2, DKFZP434N1526, kappaB-Ras2 |
| Gene groups (HGNC) | RAS type GTPase family |
| Reactome | 27 pathways, smallest: RIP-mediated NFkB activation via ZBP1; ZBP1(DAI) mediated induction of type I IFNs; TRAF6 mediated NF-kB activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYR9](https://www.uniprot.org/uniprotkb/Q9NYR9) (NF-kappa-B inhibitor-interacting Ras-like protein 2):

> Atypical Ras-like protein that acts as a potent regulator of NF-kappa-B activity by preventing the degradation of NF-kappa-B inhibitor beta (NFKBIB) by most signals, explaining why NFKBIB is more resistant to degradation. May act by blocking phosphorylation of NFKBIB and nuclear localization of p65/RELA NF-kappa-B subunit. It is unclear whether it acts as a GTPase. Both GTP- and GDP-bound forms block phosphorylation of NFKBIB (By similarity).

**Summary**, from NCBI Gene [28511](https://www.ncbi.nlm.nih.gov/gene/28511):

> Predicted to enable GTPase activating protein binding activity. Predicted to be involved in Ral protein signal transduction. Predicted to act upstream of or within several processes, including lung alveolus development; regulation of signal transduction; and surfactant homeostasis. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17898) · Entrez [28511](https://www.ncbi.nlm.nih.gov/gene/28511) · UniProt [Q9NYR9](https://www.uniprot.org/uniprotkb/Q9NYR9) · Ensembl [ENSG00000168256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168256)

## Data

Gene col 9618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9618); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9618]; `tensor/DDL_lfc|DDL_z.npy` [9618]; `embed/gene_vectors.npy` [9618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9618 or target_col == 9618). Every well: [[NKIRAS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKIRAS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
