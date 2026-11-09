---
symbol: "UBXN1"
type: "gene"
col: 8488
ensembl_id: "ENSG00000162191"
name: "UBX domain protein 1"
location: "11q12.3"
module: 74
arm: "+"
pooled_cpm: 35.81
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# UBXN1

*UBX domain protein 1* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +7.8, q 5e-12, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 2.00× (z +6.2, q 1e-07, up in 46 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.250×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYF2]] (+0.76, fdr 7e-06), [[NOP53]] (+0.72, fdr 7e-06), [[UBE2B]] (+0.69, fdr 1e-05); moves opposite to [[NME1]] (-0.63, fdr 1e-05), [[UBE2N]] (-0.58, fdr 3e-05), [[TUBA1B]] (-0.58, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8488.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.93×** | +7.8 | 5e-12 | 42/48 (J82, A-172, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.20×** | +6.5 | 2e-08 | 35/44 (A549, LoVo, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +6.2 | 1e-07 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +6.1 | 1e-07 | 45/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +6.1 | 1e-07 | 46/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.81×** | +5.1 | 3e-05 | 35/48 (PANC-1, J82, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.74×** | +5.0 | 4e-05 | 39/46 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.78×** | +5.0 | 4e-05 | 28/38 (A-172, NCI-H460, …) | all doses, flat | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +5.0 | 4e-05 | 13/48 (J82, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.72×** | +4.5 | 4e-04 | 28/42 (KATO III, SW480, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.61×** | +4.2 | 0.001 | 38/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.2 | 0.001 | 34/47 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.56×** | +3.9 | 0.003 | 29/47 (PANC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.55×** | +3.8 | 0.007 | 31/47 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.007 | 32/47 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.007 | 34/47 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.007 | 26/48 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.009 | 29/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.013 | 29/47 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +3.2 | 0.032 | 26/48 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8488.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.250×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.692× | -3.4 | 0.40 | 25/48 (SW1417, AsPC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.0) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[A549 (line)]] | wt | 34.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.5) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[J82 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +10.7) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[PANC-1 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.1) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[SHP-77 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 8 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYF2]] | +0.76 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[NOP53]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[UBE2B]] | +0.69 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[RAB13]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[WDR48]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[SNHG32]] | +0.66 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[GPX4]] | +0.64 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[RB1CC1]] | +0.63 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[CIR1]] | +0.63 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[FRG1]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[IK]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZFAND2B]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME1]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[UBE2N]] | -0.58 | -0.43 / -0.66 | both halves | 3e-05 | pathway: DNA Double Strand Break Response |
| [[TUBA1B]] | -0.58 | -0.68 / -0.52 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[NUDT15]] | -0.56 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[PPIA]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.55 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[ELOVL6]] | -0.55 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[BRI3BP]] | -0.55 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[SUV39H2]] | -0.55 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[VMA21]] | -0.54 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[PAICS]] | -0.54 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[NUP155]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.2, -47.1); signed map (-15.9, 6.1). **Vector** length 68.9, 19.9% of its response variance represented; |z| ≥ 3 in 672 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.2 | +7.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.8 | +1.6 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.4 | +1.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | +0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | UBX domain protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,676,498-62,679,117 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOC51035, 2B28, UBXD10, SAKS1 |
| Gene groups (HGNC) | UBX domain containing |
| Reactome | 6 pathways, smallest: N-glycan trimming in the ER and Calnexin/Calreticulin cycle; Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks; DNA Double Strand Break Response |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04323](https://www.uniprot.org/uniprotkb/Q04323) (UBX domain-containing protein 1):

> Ubiquitin-binding protein that plays a role in the modulation of innate immune response. Blocks both the RIG-I-like receptors (RLR) and NF-kappa-B pathways. Following viral infection, UBXN1 is induced and recruited to the RLR component MAVS. In turn, interferes with MAVS oligomerization, and disrupts the MAVS/TRAF3/TRAF6 signalosome. This function probably serves as a brake to prevent excessive RLR signaling. Interferes with the TNFalpha-triggered NF-kappa-B pathway by interacting with cellular …

**Summary**, from NCBI Gene [51035](https://www.ncbi.nlm.nih.gov/gene/51035):

> Enables several functions, including enzyme binding activity; polyubiquitin modification-dependent protein binding activity; and proteasome regulatory particle binding activity. Involved in negative regulation of protein metabolic process. Located in cytosol and endoplasmic reticulum. Part of VCP-NPL4-UFD1 AAA ATPase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18402) · Entrez [51035](https://www.ncbi.nlm.nih.gov/gene/51035) · UniProt [Q04323](https://www.uniprot.org/uniprotkb/Q04323) · Ensembl [ENSG00000162191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162191)

## Data

Gene col 8488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8488); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8488]; `tensor/DDL_lfc|DDL_z.npy` [8488]; `embed/gene_vectors.npy` [8488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8488 or target_col == 8488). Every well: [[UBXN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBXN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
