---
symbol: "CCDC107"
type: "gene"
col: 8283
ensembl_id: "ENSG00000159884"
name: "coiled-coil domain containing 107"
location: "9p13.3"
module: 54
arm: "+"
pooled_cpm: 20.48
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# CCDC107

*coiled-coil domain containing 107* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.62× (z +3.9, q 0.065, up in 28 of 44 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~45% of this change.
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.272× (z -14.7, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMTOR5]] (+0.75, fdr 7e-06), [[LIN7B]] (+0.73, fdr 1e-05), [[LSM2]] (+0.72, fdr 1e-05); moves opposite to [[ZNF655]] (-0.68, fdr 1e-05), [[NRAS]] (-0.66, fdr 9e-05), [[LIN7C]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.62×** | +3.9 | 0.065 | 28/44 (SW1417, AsPC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8283.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.272×** | -14.7 | 0e+00 | 40/47 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.354×** | -8.3 | 3e-14 | 37/47 (H4, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.490×** | -5.7 | 2e-06 | 34/48 (HS-578T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.489×** | -5.5 | 6e-06 | 28/47 (HS-578T, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.527×** | -5.1 | 4e-05 | 27/48 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.530×** | -4.9 | 1e-04 | 18/28 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -4.8 | 2e-04 | 29/47 (H4, C-33 A, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.587×** | -4.2 | 0.002 | 26/40 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.719×** | -3.7 | 0.012 | 30/48 (SW1417, KATO III, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.721×** | -3.7 | 0.013 | 27/48 (A-172, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.614×** | -3.6 | 0.016 | 20/35 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.670×** | -3.2 | 0.067 | 23/48 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.674× | -3.0 | 0.10 | 19/46 (NCI-H23, RKO, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.665× | -3.0 | 0.10 | 19/47 (SW 1271, NCI-H1792, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.410× | -3.0 | 0.10 | 22/45 (NCI-H2030, Hs 766T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 34.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0573× (z -27.0) |
| [[NCI-H23 (line)]] | alt | 58.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -21.4) |
| [[HS-578T (line)]] | alt | 39.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -18.5) |
| [[A498 (line)]] | wt | 31.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -15.5) |
| [[H4 (line)]] | wt | 31.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0362× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 25.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -18.4) |
| [[NCI-H2030 (line)]] | alt | 41.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0780× (z -23.2) |
| [[SNU-1 (line)]] | wt | 34.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0793× (z -11.2) |
| [[A-172 (line)]] | wt | 20.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -13.2) |
| [[A549 (line)]] | wt | 25.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -10.6) |
| [[C-33 A (line)]] | alt | 30.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -11.2) |
| [[HOP62 (line)]] | alt | 23.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -16.6) |
| [[hTERT-HPNE (line)]] | wt | 27.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -11.4) |
| [[J82 (line)]] | alt | 37.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 25.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -16.1) |
| [[PANC-1 (line)]] | alt | 36.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -14.0) |
| [[RKO (line)]] | wt | 15.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -14.0) |
| [[C32 (line)]] | wt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -9.4) |
| [[HCT15 (line)]] | alt | 9.93 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0831× (z -9.0) |
| [[LoVo (line)]] | wt | 8.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0866× (z -15.0) |
| [[SNU-423 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -13.8) |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.255× (z -9.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A-427 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 8 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMTOR5]] | +0.75 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[LIN7B]] | +0.73 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[LSM2]] | +0.72 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[RPP21]] | +0.72 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[NUDT22]] | +0.71 | +0.42 / +0.78 | both halves | 4e-05 |  |
| [[ARID3A]] | +0.71 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.70 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.70 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[C19orf81]] | +0.69 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MPG]] | +0.69 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[A1BG]] | +0.69 | +0.52 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | -0.68 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[NRAS]] | -0.66 | -0.36 / -0.65 | both halves | 9e-05 |  |
| [[LIN7C]] | -0.65 | -0.44 / -0.72 | both halves | 3e-05 |  |
| [[EWSR1]] | -0.64 | -0.37 / -0.68 | both halves | 7e-05 |  |
| [[EIF4G2]] | -0.64 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.63 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[TUG1]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[DARS2]] | -0.62 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.62 | -0.30 / -0.66 | both halves | 2e-04 |  |
| [[YWHAE]] | -0.62 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.61 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[SFPQ]] | -0.61 | -0.44 / -0.63 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.748). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.5, -17.8); signed map (-29.7, 11.8). **Vector** length 98.7, 28.9% of its response variance represented; |z| ≥ 3 in 644 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.53 to 9); *Mitochondrial translation* (reactome, mean cos +0.53 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | -5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +0.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.2 | -4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.1 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -14.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 107 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,658,290-35,661,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC31967 |
| Matched by | ensembl_id |

UniProt [Q8WV48](https://www.uniprot.org/uniprotkb/Q8WV48) carries no function annotation.

**Summary**, from NCBI Gene [203260](https://www.ncbi.nlm.nih.gov/gene/203260):

> This gene encodes a membrane protein which contains a coiled-coil domain in the central region. Multiple alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:28465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28465) · Entrez [203260](https://www.ncbi.nlm.nih.gov/gene/203260) · UniProt [Q8WV48](https://www.uniprot.org/uniprotkb/Q8WV48) · Ensembl [ENSG00000159884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159884)

## Data

Gene col 8283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8283); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8283]; `tensor/DDL_lfc|DDL_z.npy` [8283]; `embed/gene_vectors.npy` [8283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8283 or target_col == 8283). Every well: [[CCDC107 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC107.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
