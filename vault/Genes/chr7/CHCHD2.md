---
symbol: "CHCHD2"
type: "gene"
col: 2728
ensembl_id: "ENSG00000106153"
name: "coiled-coil-helix-coiled-coil-helix domain containing 2"
location: "7p11.2"
module: 131
arm: "+"
pooled_cpm: 119.08
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# CHCHD2

*coiled-coil-helix-coiled-coil-helix domain containing 2* — 7p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.51× (z +6.2, q 3e-07, up in 41 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.60× (z +3.4, q 0.038, up in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 6.53×, A549 4.95×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.340×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0827×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS15]] (+0.77, fdr 7e-06, ⚠ RPS15 in the vector space only through flagged drug-doses), [[SNRPD2]] (+0.76, fdr 7e-06), [[RPS21]] (+0.76, fdr 7e-06), [[RPS23]] (+0.75, fdr 7e-06); moves opposite to [[MED12]] (-0.62, fdr 2e-05), [[SRRM2]] (-0.61, fdr 1e-05), [[ARFGAP2]] (-0.60, fdr 2e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2728.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 6.53×, A549 4.95×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.51×** | +6.2 | 3e-07 | 41/45 (NCI-H1573, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.37×** | +6.1 | 3e-07 | 39/43 (NCI-H1573, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.94×** | +5.3 | 2e-05 | 46/49 (NCI-H1573, SNU-1, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.92×** | +4.8 | 2e-04 | 46/48 (PANC-1, SW480, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.0 | 0.007 | 38/47 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +3.5 | 0.037 | 5/50 (KATO III, BT-474, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +3.4 | 0.038 | 38/48 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.60×** | +3.4 | 0.038 | 31/48 (CFPAC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.038 | 41/49 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | 1.54× | +3.0 | 0.14 | 38/48 (SNU-423, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2728.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.340×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0827×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.728× | -3.3 | 0.57 | 29/48 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 137 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.4) |
| [[A549 (line)]] | wt | 82.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1573 (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.53× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW 1271 (line)]] | alt | 78.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0827× (z -8.8) |
| [[A-172 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 220 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 127 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 265 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 104 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 154 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 96.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 214 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 144 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 156 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS15]] ⚠ | +0.77 | +0.72 / +0.73 | both halves | 7e-06 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[SNRPD2]] | +0.76 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[RPS21]] | +0.76 | +0.69 / +0.72 | both halves | 7e-06 | pathway: Protein localization |
| [[RPS23]] | +0.75 | +0.72 / +0.70 | both halves | 7e-06 | pathway: Protein localization |
| [[TRMT112]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[RPS11]] | +0.73 | +0.71 / +0.69 | both halves | 7e-06 | pathway: Protein localization |
| [[RPL28]] | +0.73 | +0.66 / +0.69 | both halves | 7e-06 | pathway: Protein localization |
| [[RPL8]] ⚠ | +0.72 | +0.64 / +0.70 | both halves | 7e-06 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[RPL38]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 | pathway: Protein localization |
| [[FAU]] | +0.72 | +0.53 / +0.77 | both halves | 1e-05 | pathway: Protein localization |
| [[RPS10]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 | pathway: Protein localization |
| [[RPS25]] | +0.71 | +0.59 / +0.68 | both halves | 7e-06 | pathway: Protein localization |
| [[RPL32]] | +0.70 | +0.65 / +0.64 | both halves | 7e-06 | pathway: Protein localization |
| [[RPLP2]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 | pathway: Protein localization |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED12]] | -0.62 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[SRRM2]] | -0.61 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ARFGAP2]] | -0.60 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[BMI1]] | -0.59 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[EIF2B5]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[UBAP2L]] | -0.58 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[TIA1]] | -0.58 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[HNRNPU]] | -0.57 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[STRN4]] | -0.57 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[HNRNPL]] | -0.57 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[PRRC2A]] | -0.57 | -0.38 / -0.64 | both halves | 7e-05 |  |
| [[ATP13A1]] | -0.56 | -0.41 / -0.61 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-48.0, -26.7); signed map (-62.3, -2.5). **Vector** length 74.9, 35.8% of its response variance represented; |z| ≥ 3 in 531 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.71 to 20); *Peptide chain elongation* (reactome, mean cos +0.70 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.70 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.2 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | +2.2 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.6 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -2.7 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -2.7 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -2.6 | +6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -0.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.7 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil-helix-coiled-coil-helix domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p11.2 — chr7:56,101,573-56,106,476 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MIX17B, MNRR1; previously C7orf17 |
| Gene groups (HGNC) | Coiled-coil-helix-coiled-coil-helix domain containing proteins |
| Reactome | 3 pathways, smallest: Mitochondrial protein import; Mitochondrial protein degradation; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6H1](https://www.uniprot.org/uniprotkb/Q9Y6H1) (Coiled-coil-helix-coiled-coil-helix domain-containing protein 2):

> Transcription factor. Binds to the oxygen responsive element of COX4I2 and activates its transcription under hypoxia conditions (4% oxygen), as well as normoxia conditions (20% oxygen).

**Summary**, from NCBI Gene [51142](https://www.ncbi.nlm.nih.gov/gene/51142):

> The protein encoded by this gene belongs to a class of eukaryotic CX(9)C proteins characterized by four cysteine residues spaced ten amino acids apart from one another. These residues form disulfide linkages that define a CHCH fold. In response to stress, the protein translocates from the mitochondrial intermembrane space to the nucleus where it binds to a highly conserved 13 nucleotide oxygen responsive element in the promoter of cytochrome oxidase 4I2, a subunit of the terminal enzyme of the …

**Accessions** — [HGNC:21645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21645) · Entrez [51142](https://www.ncbi.nlm.nih.gov/gene/51142) · UniProt [Q9Y6H1](https://www.uniprot.org/uniprotkb/Q9Y6H1) · Ensembl [ENSG00000106153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106153)

## Data

Gene col 2728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2728); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2728]; `tensor/DDL_lfc|DDL_z.npy` [2728]; `embed/gene_vectors.npy` [2728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2728 or target_col == 2728). Every well: [[CHCHD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHCHD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
