---
symbol: "SLC39A7"
type: "gene"
col: 3372
ensembl_id: "ENSG00000112473"
name: "solute carrier family 39 member 7"
location: "6p21.32"
module: 42
arm: "+"
pooled_cpm: 48.8
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SLC39A7

*solute carrier family 39 member 7* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.43× (z +5.3, q 7e-05, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.522× (z -9.6, q 4e-19, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLT1B]] (+0.77, fdr 7e-06), [[SRPRA]] (+0.74, fdr 7e-06), [[SURF4]] (+0.73, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.3 | 7e-05 | 30/48 (BT-474, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.7 | 5e-04 | 32/47 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +4.7 | 5e-04 | 29/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.038 | 23/48 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.048 | 18/48 (SW 900, COLO 205, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.18 | 18/48 (RPMI-7951, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.23× | +3.1 | 0.18 | 20/48 (NCI-H2030, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.522×** | -9.6 | 4e-19 | 40/48 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.601×** | -7.5 | 1e-11 | 38/48 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.692×** | -7.3 | 6e-11 | 36/48 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.613×** | -7.2 | 6e-11 | 36/48 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.609×** | -7.0 | 2e-10 | 37/48 (J82, HepG2/C3A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.646×** | -6.2 | 5e-08 | 36/48 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.703×** | -5.2 | 1e-05 | 28/48 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.782×** | -4.9 | 8e-05 | 27/48 (hTERT-HPNE, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.724×** | -4.8 | 1e-04 | 26/47 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -4.3 | 1e-03 | 28/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.770×** | -3.9 | 0.005 | 26/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **0.790×** | -3.5 | 0.023 | 20/48 (LOX-IMVI, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.794×** | -3.4 | 0.028 | 15/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.658×** | -3.2 | 0.048 | 18/49 (SW48, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.798×** | -3.2 | 0.049 | 18/48 (RKO, NCI-H23, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.854× | -3.2 | 0.049 | 15/48 (Hs 766T, KATO III, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.815×** | -3.0 | 0.084 | 19/48 (hTERT-HPNE, COLO 205, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 67.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 76.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.0) |
| [[H4 (line)]] | wt | 83.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -9.3) |
| [[HOP62 (line)]] | alt | 61.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.379× (z -9.7) |
| [[HS-578T (line)]] | alt | 87.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.364× (z -9.8) |
| [[HT-29 (line)]] | alt | 55.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 75.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -10.5) |
| [[KATO III (line)]] | alt | 94.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 52.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -10.4) |
| [[SW 900 (line)]] | alt | 58.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.281× (z -10.9) |
| [[A-172 (line)]] | wt | 46.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AsPC-1 (line)]] | alt | 47.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.341× (z -9.8) |
| [[BT-474 (line)]] | alt | 44.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 54.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 53.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.265× (z -9.7) |
| [[J82 (line)]] | alt | 44.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.304× (z -10.4) |
| [[LoVo (line)]] | wt | 53.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.386× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 38.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.9) |
| [[RKO (line)]] | wt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[SW1417 (line)]] | alt | 43.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.395× (z -8.6) |
| [[A-427 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLT1B]] | +0.77 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[SRPRA]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SURF4]] | +0.73 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[TMED2]] | +0.71 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.70 | +0.77 / +0.71 | both halves | 7e-06 | STRING 579 |
| [[COPB2]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[HDLBP]] | +0.68 | +0.77 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[COPG1]] | +0.68 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[HYPK]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SAR1A]] | +0.66 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[TMEM214]] | +0.65 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[HYOU1]] | +0.65 | +0.69 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, -30.3); signed map (-55.5, 8.5). **Vector** length 113, 31.0% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.56 to 11); *Asparagine N-linked glycosylation* (reactome, mean cos +0.50 to 23); *Maturation of DENV proteins* (reactome, mean cos +0.53 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -1.2 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | +0.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | -1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -2.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 39 member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,200,305-33,204,439 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H2-KE4, D6S2244E, KE4, RING5, ZIP7; previously HKE4 |
| Gene groups (HGNC) | Solute carrier family 39 |
| Reactome | 5 pathways, smallest: Zinc influx into cells by the SLC39 gene family; Zinc transporters; Metal ion SLC transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92504](https://www.uniprot.org/uniprotkb/Q92504) (Zinc transporter SLC39A7):

> Transports Zn(2+) from the endoplasmic reticulum (ER)/Golgi apparatus to the cytosol, playing an essential role in the regulation of cytosolic zinc levels. Acts as a gatekeeper of zinc release from intracellular stores, requiring post-translational activation by phosphorylation, resulting in activation of multiple downstream pathways leading to cell growth and proliferation. Has an essential role in B cell development and is required for proper B cell receptor signaling. Plays an important role …

**Summary**, from NCBI Gene [7922](https://www.ncbi.nlm.nih.gov/gene/7922):

> The protein encoded by this gene transports zinc from the Golgi and endoplasmic reticulum to the cytoplasm. This transport may be important for activation of tyrosine kinases, some of which could be involved in cancer progression. Therefore, modulation of the encoded protein could be useful as a therapeutic agent against cancer. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:4927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4927) · Entrez [7922](https://www.ncbi.nlm.nih.gov/gene/7922) · UniProt [Q92504](https://www.uniprot.org/uniprotkb/Q92504) · Ensembl [ENSG00000112473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112473)

## Data

Gene col 3372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3372); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3372]; `tensor/DDL_lfc|DDL_z.npy` [3372]; `embed/gene_vectors.npy` [3372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3372 or target_col == 3372). Every well: [[SLC39A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC39A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
